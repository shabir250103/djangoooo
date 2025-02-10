import os
import json
import firebase_admin
from firebase_admin import credentials

# Load Firebase credentials from environment variable
firebase_creds = os.getenv("FIREBASE_CREDENTIALS")
if firebase_creds:
    creds_dict = json.loads(firebase_creds)
    cred = credentials.Certificate(creds_dict)
    firebase_admin.initialize_app(cred)
else:
    raise ValueError("Firebase credentials not found in environment variables!")
