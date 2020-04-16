from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
# from home.models import Branch,About, SpecialityMenu
import requests

from user_auth.models import Customer
from django.contrib.auth.decorators import login_required
import json


# Create your views here.

def homePage(request):

    context = {}
    # about = About.objects.get(name='Paradise')
    request_body = {"app":"home","model":"About","operation":"readall"}

    response = requests.post("http://127.0.0.1:8000/api/read", json=request_body)

    if response.status_code == 200:

        about = response.json()['response']
        context['about'] = about[0]

    else:
        print("Oops About Section Error")

    # branches = Branch.objects.all()
    request_body = {"app":"home","model":"Branch","operation":"readall"}

    response = requests.post("http://127.0.0.1:8000/api/read", json=request_body)

    if response.status_code == 200:

        branches = response.json()['response']
        context['branches'] = branches

    else:
        print("Oops Branch Section Error")
    

    # specials = SpecialityMenu.objects.all()
    request_body = {"app":"home","model":"SpecialityMenu","operation":"readall"}

    response = requests.post("http://127.0.0.1:8000/api/read", json=request_body)

    if response.status_code == 200:

        specials = response.json()['response']
        context['specials'] = specials

    else:
        print("Oops Branch Section Error")

    return render(request,"home/home.html",context)


@login_required(login_url='/auth/login/')
def personalise(request):

    if request.method =='POST':

        try:
            calorieLimit = int(request.POST.get('calorielimit'))
            time = int(request.POST.get('time'))
            budget = int(request.POST.get('budget'))
            cuisineType = request.POST.get('cuisineType')
            vnv = request.POST.get('vnv')
            rating = 8

            if cuisineType == 'north':
                cuisineType = 1
            else:
                cuisineType = 0

            if vnv == 'veg':
                vnv = 1
            else:
                vnv = 0

            recommend = []
            recommend.append(calorieLimit)
            recommend.append(cuisineType)
            recommend.append(time)
            recommend.append(rating)
            recommend.append(budget)
            recommend.append(vnv)

            cuser = Customer.objects.get(user=request.user)
            # print(cuser.recommendation)
            cuser.recommendation = recommend
            cuser.save()

            data = json.dumps(recommend)
            request_body = {"data":data}

            response = requests.post("http://127.0.0.1:8000/api/recommend", json=request_body)

            if response.status_code == 200:

                psnl_menu = response.json()['recommend_list']
                # print(psnl_menu)
                cuser.personalised_menu = psnl_menu

                cuser.save()

            else:
                print("Oops Recommendation Error")

        except:
            return render(request, 'home/personalise.html', {})
            
        return HttpResponseRedirect(reverse('menu:menu'))

    else:
        context = {}
        return render(request, 'home/personalise.html', context)


def redirectHome(request):
    return HttpResponseRedirect(reverse('home:home'))