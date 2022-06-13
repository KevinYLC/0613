import requests , json
import firebase_admin
import zlib
from firebase_admin import credentials ,firestore

cred = credentials.Certificate('testkey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("test")


asd= db.collection("test").document("key")

asdf = asd.get().to_dict()['2022-06-13']
# asd = zlib.compress(asdf.decode("utf-8"))
# .decode('uft-8')  
asdfg = zlib.decompress(asdf).decode("utf-8")
print(asdfg)