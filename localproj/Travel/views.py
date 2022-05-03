from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

def testlang(request):
    return HttpResponse(_('Welcome to language translation'))

def index(request):
    return render(request, 'index.html')

def hotel(request):
    return render(request, 'hotel.html')


def Flights(request):
    return render(request, 'Flights.html')


def Tours(request):
    return render(request, 'Tours.html')


def ContactUs(request):
    return render(request, 'ContactUs.html')


