"""
Chatroom application views

"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from chatroom.models import ChatRoomMessageModel


def index(request: HttpRequest) -> HttpResponse:
    """Index page view"""

    return render(request, "index.html")


def chatroom(request: HttpRequest, room_id: str) -> HttpResponse:
    """Chat room view"""

    ctx = {
        "room_id": room_id,
        "object_list": ChatRoomMessageModel.objects.filter(group_name=room_id),
    }

    return render(request, "chatroom.html", ctx)
