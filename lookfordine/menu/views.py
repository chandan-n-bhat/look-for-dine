from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from menu.models import Menu
import requests
from django.contrib.auth.decorators import login_required


# Create your views here.

# @csrf_exempt
@login_required(login_url='/auth/login/')
def showMenu(request):

    request_body = {"app":"menu","model":"Menu","operation":"readall"}

    response = requests.post("http://127.0.0.1:8000/api/read", json=request_body)

    if(response.status_code == 200):
        menu_list = response.json()['response']
        breakfast_list = []
        biryani_list = []
        chat_list = []
        curry_list = []
        dessert_list = []
        drink_list = []
        indian_bread_list = []
        meal_list = []
        salad_list = []
        soup_list = []
        starter_list = []

        for menu in menu_list:
            if(menu['cuisineType'] == 'Biryani'):
                biryani_list.append(menu)

            elif(menu['cuisineType'] == 'Breakfast'):
                breakfast_list.append(menu)

            elif(menu['cuisineType'] == 'Chat'):
                chat_list.append(menu)

            elif(menu['cuisineType'] == 'Curry'):
                curry_list.append(menu)

            elif(menu['cuisineType'] == 'Dessert'):
                dessert_list.append(menu)

            elif(menu['cuisineType'] == 'Drink'):
                drink_list.append(menu)

            elif(menu['cuisineType'] == 'Indian Bread'):
                indian_bread_list.append(menu)

            elif(menu['cuisineType'] == 'Meal'):
                meal_list.append(menu)

            elif(menu['cuisineType'] == 'Salad'):
                salad_list.append(menu)

            elif(menu['cuisineType'] == 'Soup'):
                soup_list.append(menu)

            elif(menu['cuisineType'] == 'Starter'):
                starter_list.append(menu) 

            else:
                pass

        context = {
            'menu_list':[
                {'list':breakfast_list,'type':'Breakfast'},
                {'list':starter_list,'type':'Starters'},
                {'list':soup_list,'type':'Soups'},
                {'list':salad_list,'type':'Salads'},
                {'list':biryani_list,'type':'Biryanis'},
                {'list':indian_bread_list,'type':'Indian Breads'},
                {'list':curry_list,'type':'Currys'},
                {'list':dessert_list,'type':'Desserts'},
                {'list':chat_list,'type':'Chats'},
                {'list':meal_list,'type':'Meals'}

            ]
        }
        return render(request,'menu/menu.html',context)
    else:
        return HttpResponse("Oops Something went Wrong!!")
    

