from django.urls import path
from .views import *

urlpatterns = [
    path("verify-token/", verify_firebase_token, name="verify-token"),
    path("send-notification/", send_push_notification, name="send-notification"),
    path('', firebase_view, name='firebase_home'),
]
