from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import numpy as np

# Create your views here.

@csrf_exempt
def readDb(request):

    json_body = json.loads(request.body)

    if(request.method == 'POST'):
        operation = json_body['operation']
        app = json_body['app']
        c_model = json_body['model']

        if(operation == 'readall'):
        
            cur_model = apps.get_model(app,c_model)
            querySet = cur_model.objects.all().values()
            response = {'response':list(querySet)}
            return JsonResponse(response, safe=False, status=200)
        
    else:
        return JsonResponse({'Error':'Invalid Method'}, safe=False, status=400)

@csrf_exempt
def changeImage(request):

    # json_body = json.loads(request.body)

    if request.method == 'GET':

        # id = json_body['id']
        # app = json_body['app']
        # c_model = json_body['model']
        id = request.GET.get('id')
        app = request.GET.get('app')
        c_model = request.GET.get('model')

        cur_model = apps.get_model(app,c_model)

        # querySet = cur_model.objects.get(id=id).value('image')
        # print(querySet)
        # response = {'imageUrl':querySet}

        instance = cur_model.objects.get(id=id)
        value = getattr(instance,'image')

        response = {'imageUrl':value}

        return JsonResponse(response, safe=False, status=200)

    else:
        return JsonResponse({"error":"Wrong Method"}, safe=False, status=400)


def checkUsername(request):

    username = request.GET['username']
    
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }

    return JsonResponse(data, status=200)

def getMap(request):

    if request.method == 'GET':

        data = {
            "state":"success",
            "map1": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.7396086477806!2d77.53556311463579!3d12.988499418021993!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3dbfc721a48f%3A0x91afe29a6a4d4716!2sShanthi%20Sagar%2C%20Basaveshwara%20nagar!5e0!3m2!1sen!2sin!4v1586940102603!5m2!1sen!2sin",
            "map2": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15550.347566568782!2d77.5607356697754!3d12.998253499999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1625bc6a63f3%3A0x6941d824e3c07d0b!2sCentral%20Tiffin%20Room!5e0!3m2!1sen!2sin!4v1587028117587!5m2!1sen!2sin",
            "map3": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.4180908714698!2d77.56915431463541!3d12.945077218962687!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae15f2e88ad035%3A0xed7fede7791f8edc!2sVidyarthi%20Bhavan!5e0!3m2!1sen!2sin!4v1587042261459!5m2!1sen!2sin"
        }

        return JsonResponse(data, status=200)
    
    else:
        return JsonResponse({}, status=400)

def getHomeImages(request):

    if request.method == 'GET':

        data = {
            "status": "success",
            "aboutImage": "/static/home/images/tablesetting2.jpg",
            "branchImage": "/static/home/images/tablesetting.jpg",
            "specialImage": "/static/home/images/tablesetting4.jpg"
        }

        return JsonResponse(data, status=200)

    else:
        return JsonResponse({}, status=400)

@csrf_exempt
def recommendMenu(request):

    json_body = json.loads(request.body)
    if request.method == 'POST':

        data = json_body['data']

        point = json.loads(data)
        # print(point)
        recommend_list = recommend(point,X,Y)

        return JsonResponse({'recommend_list':recommend_list}, status=200)

    else:
        return JsonResponse({}, status=400)


def f(point, data, labels, k):
    n_of_dimensions = len(point)
    neighbors = []
    neighbor_labels = []
    for i in range(0, k):
        nearest_neighbor_id = None
        smallest_distance = None
        for i in range(0, len(data)):
            eucledian_dist = 0
            for d in range(0, n_of_dimensions):
                dist = abs(point[d] - data[i][d])
                eucledian_dist += dist
            eucledian_dist = np.sqrt(eucledian_dist)
            if smallest_distance == None:
                smallest_distance = eucledian_dist
                nearest_neighbor_id = i
            elif smallest_distance > eucledian_dist:
                smallest_distance = eucledian_dist
                nearest_neighbor_id = i
                
        neighbors.append(data[nearest_neighbor_id])
        neighbor_labels.append(labels[nearest_neighbor_id])
        
        data.remove(data[nearest_neighbor_id])
        labels.remove(labels[nearest_neighbor_id])
    return neighbor_labels


def func(point):
    l=list()
    for i in range(0,len(X)):
        dist=((1/(point[0]-X[i][0]+0.00000001))*(point[0]-X[i][0])**2+(1/(point[1]-X[i][1]+0.00000001))*(point[1]-X[i][1])**2+(1/(point[2]-X[i][2]+0.00000001))*(point[2]-X[i][2])**2+(1/(point[3]-X[i][3]+0.00000001))*(point[3]-X[i][3])**2+(1/(point[4]-X[i][4]+0.00000001))*(point[4]-X[i][4])**2)**2
        l.append(dist)
    K=10
    res = sorted(range(len(l)), key = lambda sub: l[sub])[:10]
    recommendations=list()
    for i in res:
        recommendations.append(Y[i])
    return recommendations


def recommend(point, data, labels, k=1):
    while True:
        labels = f(point, data, labels, k=k)
        label = most_found(labels)
        if label != None:
            break
        k += 1
        if k >= len(data):
            break
    return func(point)

def most_found(array):
    list_of_words = []
    for i in range(len(array)):
        if array[i] not in list_of_words:
            list_of_words.append(array[i])
    most_counted = ''
    n_of_most_counted = None
    for i in range(len(list_of_words)):
        counted = array.count(list_of_words[i])
        if n_of_most_counted == None:
            most_counted = list_of_words[i]
            n_of_most_counted = counted
        elif n_of_most_counted < counted:
            most_counted = list_of_words[i]
            n_of_most_counted = counted
        elif n_of_most_counted == counted:
            most_counted = None
    return most_counted


X=[
    [60,0,15,8,70,1],
    [70,1,20,7,85,1],
    [80,1,18,9,60,1],

    [220,1,15,8,90,1],
    [210,1,10,9,100,1],
    [100,1,10,9,120,1],

    [150,1,20,6,90,1],
    [170,1,15,7,100,1],
    [180,1,18,8,80,1],
    [140,1,20,9,110,1],
    [180,1,20,9,100,1],
    [150,1,18,8,80,1],

    [50,0,15,9,30,1],
    [40,0,18,9,20,1],
    [80,0,20,8,50,1],
    [70,0,20,8,60,1],
    [60,0,25,9,45,1],
    [85,1,20,8,65,1],
    [80,0,20,7,50,1],
    [120,1,18,6,70,1],

    [50,1,2,9,40,1],
    [50,1,1,10,50,1],
    [60,1,5,10,50,1],
    [70,1,8,9,40,1],
    [85,1,10,8,50,1],
    [90,1,10,9,40,1],
    [90,1,9,10,55,1],
    [40,1,9,12,40,1],

    [10,0,10,10,25,1],
    [15,0,9,6,45,1],
    [15,0,8,5,40,1],

    [120,1,7,6,75,1],
    [110,0,8,7,55,1],
    [100,1,9,6,85,1],
    [90,1,8,5,100,1],
    [70,1,9,4,90,1],

    [155,1,9,7,345,1],
    [170,1,10,8,245,1],
    [180,1,10,9,200,1],
    [200,1,10,10,300,1],
    [410,1,9,10,300,1],
    [300,1,5,10,440,0],

    [200,1,6,5,125,1],
    [250,1,4,10,180,1],
    [300,1,5,10,280,0],
    [200,0,7,9,110,1],

    [400,1,3,9,100,1],
    [200,0,8,8,120,1],

    [40,1,5,7,10,1],
    [60,1,7,7,15,1],
    [50,0,4,8,20,1]
]

Y=[
    'Tomato Soup',
    'Baby Corn Soup',
    'Veg Soup',

    'Vegetable Salad',
    'Fruit Salad',
    'Paradise Salad',

    'Gobi Manchurian',
    'Baby Corn Manchurian',
    'Veg Manchurian',
    'Paneer Manchurian',
    'Paneer Tikka',
    'Aloo Manchurian',

    'Idly',
    'Vada',
    'Masala Dosa',
    'Onion Dosa',
    'Poori Saagu',
    'Chole Bature',
    'Chow Chow Bath',
    'Aloo Parata',

    'Pani Puri',
    'Sev Puri',
    'Bhel Puri',
    'Masala Puri',
    'Samosa Chat',
    'Dahi Puri',
    'Raj Kachori',
    'Vada Pav',

    'Desi Chai',
    'Coffee',
    'Badam Milk',

    'Rabdi',
    'Gulab Jamun',
    'Ras Malai',
    'Paradise Pastry',
    'Choco Lava Cake',

    'Veg Biryani',
    'Jeera Rice',
    'Fried Rice',    
    'Schezwan Fried Rice',
    'Dum Biryani',
    'Chicken Biryani',

    'Palak Paneer',
    'Kadai Paneer',
    'Butter Chicken',
    'Dal',

    'North Meal',
    'South Meal',

    'Roti',
    'Kulcha',
    'Kerala Parata'
]

# calories -- north/south -- time required -- rating -- cost -- veg/non-veg