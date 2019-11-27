from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from . models import *

from django.forms import ModelChoiceField,ModelForm,TextInput,Textarea


from django.db import transaction

from django.utils.translation import ugettext_lazy as _
import datetime


class FileFieldForm(forms.Form):
    ffile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
    last_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
    phone = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'})) 
    password1 = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','type' : 'password',}))   
    password2 = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','type' : 'password',}))  


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name','last_name','email','username')
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Re-Type Password"
        self.fields['dob'].label = "Date of Birth"

    @transaction.atomic    
    def save(self):        
        user = super().save(commit=False)
        user.is_doctor = True
        

        user.save()    
        


        # user.role.set(range(Role.DOCTOR))     
        doctor = Doctor.objects.create(user=user)  
        Employee.objects.create(user=user)  
        # doctor.departmentname.add(*self.get('departmentname'))    
        # doctor.usericon.add(*self.get('usericon'))    
            
        return doctor
