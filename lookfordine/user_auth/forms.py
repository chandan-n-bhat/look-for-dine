from django import forms
from django.contrib.auth.models import User
from user_auth.models import Customer

class CustomerForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input100','id':'username','onblur':'obj.checkUnameAvailable()'}))

    class Meta():
        model = User
        fields = ('username','password')

class ProfileForm(forms.ModelForm):

    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'input100'}))

    class Meta():
        model = Customer
        fields = ('email',)
