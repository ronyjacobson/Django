from django import forms
from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
     class Meta:
         model = User
         fields = ['facebook_id', 'first_name', 'last_name','email', 'birthday']



class SPForm(ModelForm):
   class Meta:
         model = SP
         fields = ['name', 'desc', 'address', 'city' , 'longitude',
                   'latitude', 'phone', 'discount', 'category', 'website']