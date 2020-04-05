from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from user_auth.forms import CustomerForm, ProfileForm
from django.contrib.auth.models import User

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

import json

# Create your views here.

def customer_login(request):

    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username,password=password)

        if(user):
            if(user.is_active):
                login(request,user)
                return HttpResponseRedirect(reverse('menu:menu'))
            else:
                return HttpResponse("User Not Active")
        
        else:
            print("A Login attempt failed")
            print("Username {} and Password {}".format(username,password))
            return HttpResponse("Invalid Credentials")

    else:
        return render(request, 'user_auth/login.html', {})

@login_required
def customer_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:home'))

def signup(request):

    registered = False

    if(request.method == 'POST'):

        user_form = CustomerForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if(user_form.is_valid()):

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            # profile.user = user

            # if('profile_pic' in request.FILES):
            #     profile.profile_pic = request.FILES['profile_pic']

            # profile.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        
        else:
            print(user_form.errors)
    
    else:

        user_form = CustomerForm()
        profile_form = ProfileForm()
    
    return render(request, 'user_auth/signup.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def getUsers(request):

    username = request.GET.get('username')
    users = User.objects.all().values_list('username',flat=True)

    users = list(users)
    # return JsonResponse({'a':users},safe=False)

    if(username in users):
        return JsonResponse({'availability':'false'})
    
    else:
        return JsonResponse({'availability':'true'})
