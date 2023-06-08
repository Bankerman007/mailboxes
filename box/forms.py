from django import forms
from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email', 'address']
        name = forms.CharField()
        email = forms.CharField()
        address = forms.CharField()