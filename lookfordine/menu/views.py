from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.

def showMenu(request):
    return HttpResponse("Menu")