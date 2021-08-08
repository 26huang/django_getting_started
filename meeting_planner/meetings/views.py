from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room

# Create your views here.

def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms(request):
    return render(request, "meetings/rooms_info.html", {"rooms": Room.objects.all()})