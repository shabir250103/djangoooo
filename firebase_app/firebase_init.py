import firebase_admin
from firebase_admin import credentials

# 🔹 Load Firebase Credentials
FIREBASE_CONFIG_PATH = "D:/a/myproject/firebase_app/service.json"

# 🔹 Initialize Firebase App
cred = credentials.Certificate(FIREBASE_CONFIG_PATH)
firebase_admin.initialize_app(cred)
