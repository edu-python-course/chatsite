"""
Chatroom application views

"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Index page view"""

    return render(request, "index.html")


def chatroom(request: HttpRequest, room_id: str) -> HttpResponse:
    """Chat room view"""

    return render(request, "chatroom.html", {"room_id": room_id})
