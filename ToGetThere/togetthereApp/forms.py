from django import forms
from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
     class Meta:
         model = User
         fields = ['facebook_id', 'first_name', 'last_name','email', 'birthday']



class AddSPForm(ModelForm):
    class Meta:
         model = SP
         fields = ['name', 'desc', 'category', 'city', 'street', 'street_num', 'longitude',
                   'latitude', 'phone', 'discount', 'website']

#class RankSPForm(ModelForm):



#class EditSPForm(ModelForm):


class AddReviewForm(ModelForm):
    class Meta:
         model = Review
         fields = ['title', 'content', 'user']