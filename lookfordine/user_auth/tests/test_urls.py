from django.test import SimpleTestCase
from django.urls import resolve, reverse
from user_auth import views as auth_views
from menu import views as menu_views
from home import views as home_views
from book import views as book_views


class TestUrls(SimpleTestCase):

    # URLs : user_auth app
    def test_url_login(self):
        url = reverse('user_auth:login')
        self.assertEquals(resolve(url).func,auth_views.customer_login)
        print("\t test_url_login Passed")

    def test_url_logout(self):
        url = reverse('user_auth:logout')
        self.assertEquals(resolve(url).func,auth_views.customer_logout)
        print("\t test_url_logout Passed")


    def test_url_signup(self):
        url = reverse('user_auth:signup')
        self.assertEquals(resolve(url).func,auth_views.signup)
        print("\t test_url_signup Passed")


    # URLs : home app
    def test_url_home(self):
        url = reverse('home:home')
        self.assertEquals(resolve(url).func,home_views.homePage)
        print("\n\nUnit test - URLs")
        print("\n\t test_url_home Passed")


    def test_url_personalise(self):
        url = reverse('home:personalise')
        self.assertEquals(resolve(url).func,home_views.personalise)
        print("\t test_url_personalise Passed")


    # URLs : book app
    def test_url_reserve(self):
        url = reverse('book:reserve')
        self.assertEquals(resolve(url).func,book_views.reserveTable)
        print("\t test_url_reserve Passed")


    def test_url_status(self):
        url = reverse('book:status')
        self.assertEquals(resolve(url).func,book_views.checkStatus)
        print("\t test_url_status Passed")


    # URLs : menu app
    def test_url_menu(self):
        url = reverse('menu:menu')
        self.assertEquals(resolve(url).func,menu_views.showMenu)
        print("\t test_url_menu Passed")
 