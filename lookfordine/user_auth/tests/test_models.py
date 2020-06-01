from django.test import TestCase
from django.contrib.auth.models import User
from user_auth import models as user_models
from book import models as book_models
import json

class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            username='newuser01',
            password='newpassword01'
        )

        self.user2 = User.objects.create(
            username = 'newuser02',
            password = 'newpassword02'
        )

    def test_create_customer(self):

        user_models.Customer.objects.create(
            user = self.user1,
            email = "newuser@gmail.com",
            recommendation = "",
            personalised_menu = ""
        )

        c1 = user_models.Customer.objects.get(user=self.user1)

        self.assertEquals(c1.user,self.user1)
        self.assertEquals(c1.email,"newuser@gmail.com")
        self.assertEquals(c1.recommendation,"")

        print("\t test_create_customer Passed")


    def test_create_customer_with_recommendation(self):
        recommend = [350,0,45,8,500,0]
        personalise = ["Dum Biryani","Butter Chicken","Schezwan Fried Rice","Veg Biryani","North Meal","Kadai Paneer","Jeera Rice","Fried Rice","Palak Paneer","South Meal"]


        user_models.Customer.objects.create(
            user = self.user2,
            email = "newuser2@gmail.com",
            recommendation = json.dumps(recommend),
            personalised_menu = json.dumps(personalise)
        )

        c2 = user_models.Customer.objects.get(user = self.user2)

        self.assertEquals(c2.user,self.user2)
        self.assertEquals(c2.email,"newuser2@gmail.com")

        c2_recommendation = json.loads(c2.recommendation)
        self.assertEquals(c2_recommendation,recommend)

        c2_personalise = json.loads(c2.personalised_menu)
        self.assertEquals(c2_personalise,personalise)

        print("\t test_create_customer_with_recommendation Passed")



    def test_customer_count(self):

        user_models.Customer.objects.create(
            user = self.user2,
            email = "newuser2@gmail.com",
            recommendation = "",
            personalised_menu = ""
        )

        user_models.Customer.objects.create(
            user = self.user1,
            email = "newuser2@gmail.com",
            recommendation = "",
            personalised_menu = ""
        )

        customer_count = 2
        customer_count_in_database = len(user_models.Customer.objects.all())

        self.assertEquals(customer_count,customer_count_in_database)

        print("\t test_customer_count Passed")


    def test_booking(self):
        # We will make use of user2 instance initialised in the setUp method as the user to book the table

        book_models.Booking.objects.create(
            name = "chandan",
            user = self.user2,
            branch = "Rajajinagar",
            people = 5,
            datetime = "2020-04-16 20:00",
            message = "Ambient lighting"
        )

        booked1 = book_models.Booking.objects.get(name="chandan")

        self.assertEquals(booked1.name , "chandan")
        self.assertEquals(booked1.user , self.user2)
        self.assertEquals(booked1.branch , "Rajajinagar")
        self.assertEquals(booked1.people , 5)
        self.assertEquals(booked1.message , "Ambient lighting")

        print("\n\nUnit test - Models")
        print("\t test_booking Passed")
        


    def test_check_booking_count(self):

        # Here we create multiple bookings and check if these are updated in the database by checking the count
        book_models.Booking.objects.create(
            name = "chandan",
            user = self.user2,
            branch = "Rajajinagar",
            people = 5,
            datetime = "2020-04-16 20:00",
            message = "Ambient lighting"
        )

        book_models.Booking.objects.create(
            name = "raju",
            user = self.user1,
            branch = "Vijaynagar",
            people = 2,
            datetime = "2020-04-16 20:00",
            message = "Ambient music"
        )
        
        book_models.Booking.objects.create(
            name = "harsh",
            user = self.user2,
            branch = "Malleshwaram",
            people = 8,
            datetime = "2020-04-16 20:00",
            message = "Ambient lighting"
        )

        count = len(book_models.Booking.objects.all())

        self.assertEquals(count,3)

        print("\t test_check_booking Passed")
