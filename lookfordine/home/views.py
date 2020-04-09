from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from home.models import Branch,About, SpecialityMenu

# Create your views here.

def homePage(request):

    branches = Branch.objects.all()

    about = About.objects.get(name='Paradise')
    
    specials = SpecialityMenu.objects.all()

    context = {'branches':branches,'about':about,'specials':specials}
    return render(request,"home/home.html",context)

def redirectHome(request):
    return HttpResponseRedirect(reverse('home:home'))