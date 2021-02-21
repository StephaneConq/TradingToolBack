import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': "trading-tool-305514",
})

db = firestore.client()


def get_user(email):
    user = db.collection('users').document(email).get()
    return user.to_dict() if user else None


def set_user(email, body):
    doc_ref = db.collection('users').document(email)
    doc_ref.set(body)
    return get_user(email)


def list_users():
    collection = db.collection('users').stream()
    users = []
    for user in collection:
        users.append(user.to_dict())
    return users