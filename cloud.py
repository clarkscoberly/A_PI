import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate("assetpi-firebase-adminsdk-uxgeq-219c350095.json")
firebase_admin.initialize_app(cred, {
    "projectId" : "assetpi",
})

db = firestore.client()

def add_item(item):
    data = {
        "ip" : item[0],
        "mac" : item[1],
        "manufacturer" : item[2]
    }

    db.collection("data").document(str(datetime.datetime.now())).set(data)

def get_items(timeframe):
    return db.collection("data").stream()
    