import json
import os
import firebase_admin
from firebase_admin import credentials

# Load JSON from an environment variable
firebase_config = json.loads(os.getenv("FIREBASE_CONFIG"))

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
