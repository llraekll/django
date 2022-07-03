from dataclasses import fields
import email
from enum import Flag
from pyexpat import model
from turtle import title
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                                 widget=forms.TextInput(
                                     attrs={"placeholder": "Your title"}
                                 )
                                 
                            )
    email= forms.EmailField()
    description=forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "description",
                                        "class": 'new-class-name two',
                                        'id': 'my-id-for-textarea',
                                        'rows': 20,
                                        'cols': 69
                                    }
                            )
                        )
    price= forms.DecimalField(initial=199.99, widget=forms.TextInput(
                                                attrs={"placeholder": "Gold price"}
                                            )
                                                
                                )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

#    def clean_title(self, *args, **kwargs):
 #       title = self.cleaned_data.get("title")
  #      if not "R1" in title:
  #          raise forms.ValidationError("This is not a valid title")
  #      if not "akkaya" in title:
  #          raise forms.ValidationError("This is not a valid title")
  #      return title
            
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid email")
        return email

class RawproductForm(forms.Form):
    title = forms.CharField(label='title',
                                 widget=forms.TextInput(
                                     attrs={"placeholder": "Your title"}
                                 )
                                 
                            )
    description=forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "description",
                                        "class": 'new-class-name two',
                                        'id': 'my-id-for-textarea',
                                        'rows': 20,
                                        'cols': 69
                                    }
                            )
                        )
    price= forms.DecimalField(initial=199.99,
                                    widget=forms.TextInput(
                                                attrs={"placeholder": "Your price"}
                                            )
                                                
                                )
