from dataclasses import fields
from django import forms
from .models import Product , Order

from customer.models import User


class prod_form(forms.ModelForm):

    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    

    class Meta:
        model=Product
        fields=('__all__')


class order_form(forms.ModelForm):

    class Meta:
        model=Order
        fields=('state', )

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model=User
        fields=('first_name', 'last_name', "email","address", 'phone', 'password')





