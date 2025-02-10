import os
import firebase_admin
from firebase_admin import credentials

# Get the current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path
FIREBASE_CONFIG_PATH = os.path.join(BASE_DIR, "service.json")

# Initialize Firebase
cred = credentials.Certificate(FIREBASE_CONFIG_PATH)
firebase_admin.initialize_app(cred)
