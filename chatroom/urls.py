"""
Chatroom application URL Configuration

"""

from django.urls import path

from chatroom import views

app_name = "chatroom"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_id>/", views.chatroom, name="chatroom"),
]
