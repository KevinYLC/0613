from gettext import find
import requests , json ,firebase_admin ,zlib,datetime
from firebase_admin import credentials ,firestore

with open('weatherurl.txt', 'r') as f:
    apiurl = f.read()
url = str(apiurl[:-2])
res = requests.get(url).json()

today = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
whData = res["records"]["locations"][0]["location"]

cred = credentials.Certificate('testkey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("test")
di = ""

for area in whData:
    doc_ref = db.collection("test").document("key")
    areaData = area["weatherElement"]
    di += f"{area['locationName']} \n"
    for elm in areaData:    # 地區天氣資料
        if elm["elementName"] == "WeatherDescription":  # 天氣預報綜合描述
            elmtime = elm["time"]
            # doc_ref.set("")
            for times in elmtime:
                a = times["startTime"][:-3]
                b = times["endTime"][11:-3]
                c = times["elementValue"][0]["value"]
                rec = c.find('度') + 6  
                di += f"{a} {b} {c[:rec]} \n"
code = zlib.compress(str(di).encode("utf-8"))
doc_ref.update({str(today.date()) : code})