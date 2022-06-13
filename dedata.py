import zlib ,datetime ,firebase_admin
from firebase_admin import credentials ,firestore

cred = credentials.Certificate('testkey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("test")
today = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))

asd= db.collection("test").document("key")

asdf = asd.get().to_dict()[str(today.date())]
# asd = zlib.compress(asdf.decode("utf-8"))
# .decode('uft-8')  
asdfg = zlib.decompress(asdf).decode("utf-8")
print(asdfg)