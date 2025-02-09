from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from firebase_admin import auth
from .firebase_init import *  # Import Firebase Initialization

@csrf_exempt
def verify_firebase_token(request):
    """🔹 Verify Firebase Authentication Token"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            token = data.get("idToken")  # Firebase ID Token from frontend

            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
            email = decoded_token.get("email", "")

            return JsonResponse({"message": "Token Verified!", "uid": uid, "email": email}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=401)
    return JsonResponse({"error": "Invalid request method"}, status=400)
from firebase_admin import messaging

@csrf_exempt
def send_push_notification(request):
    """🔹 Send FCM Push Notification"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            token = data.get("token")  # FCM Device Token
            title = data.get("title", "New Notification")
            body = data.get("body", "You have a new message!")

            message = messaging.Message(
                notification=messaging.Notification(title=title, body=body),
                token=token,
            )

            response = messaging.send(message)
            return JsonResponse({"message": "Notification sent!", "response": response}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)

from django.http import HttpResponse

def firebase_view(request):
    return HttpResponse("Firebase app is working!")
