from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.


def welcome(request):
    # return HttpResponse("Welcome to the meeting planner.")
    return render(request, "website/welcome.html",
                  {"message": "This is a message from view to template.",
                   "meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is Wei.")