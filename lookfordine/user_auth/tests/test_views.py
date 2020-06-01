from django.test import TestCase, Client
from django.urls import reverse
from user_auth import models as user_models
from django.contrib.auth.models import User

import json   

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()

        # user_auth urls
        self.login_url = reverse('user_auth:login')
        self.signup_url = reverse('user_auth:signup')

        # home urls
        self.home_url = reverse('home:home')
        self.personalise_url = reverse('home:personalise')

        # book urls
        self.book_url = reverse('book:reserve')

        # rest_api urls
        self.read_url = reverse('rest_api:read')
        self.check_url = reverse('rest_api:check')
        self.recommend_url = reverse('rest_api:recommend')

    # Views : user_auth app

    def test_customer_login(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'user_auth/login.html')

        print("\t test_customer_login_view Passed")
        

    def test_customer_signup(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'user_auth/signup.html')

        print("\t test_customer_signup_view Passed")


    # Views : home app

    def test_home(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home/home.html')

        print("\t test_home_view Passed")


    # Views : book app

    def test_reserve_table(self):
        response = self.client.post(self.book_url)

        self.assertEquals(response.status_code,302)

        print("\t test_reserve_table_view Passed")

    

    # Testing Rest Api's

    def test_read_api(self):

        response = self.client.post(self.read_url, json.dumps({
            "app" : 'menu',
            "model" : 'menu',
            "operation" : 'readall'
        }), content_type='application/json')

        self.assertEquals(response.status_code,200)

        print("\t test_read_api Passed")


    
    def test_check_username(self):

        response = self.client.get(self.check_url, {
            'username' : "asdf"
        }, content_type='application/json')

        self.assertEquals(response.status_code,200)

        print("\n\nUnit test - Views")
        print("\t test_check_username_api Passed")

        

    def test_recommend_post(self):

        recommend = [350,0,45,8,500,0]
        personalise = ["Dum Biryani","Butter Chicken","Schezwan Fried Rice","Veg Biryani","North Meal","Kadai Paneer","Jeera Rice","Fried Rice","Palak Paneer","South Meal"]

        user3 = User.objects.create(
            username = 'newuser03',
            password = 'newpassword03'
        )

        user_models.Customer.objects.create(
            user = user3,
            email = "newuser3@gmail.com",
            recommendation = json.dumps(recommend),
            personalised_menu = json.dumps(personalise)
        )

        customer1 = user_models.Customer.objects.get(user=user3)
        data = customer1.recommendation

        response = self.client.post(self.recommend_url, json.dumps({
            'data' : data
        }), content_type='application/json')

        self.assertEquals(response.status_code,200)

        print("\t test_recommend_post_api Passed")
        
