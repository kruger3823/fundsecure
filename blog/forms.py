from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        labels=('password1','Password','password2','Confirm_password')

class ProfileForm(forms.ModelForm):
    address=forms.CharField(max_length=200)

    class Meta:
        model=Register
        fields=('address',)



class FileUploadForm(forms.ModelForm):
    class Meta:
        model=FileUpload
        fields=('name','file')

class InsuranceApplyForm(forms.ModelForm):
    nominee_address=forms.Textarea()
    male='male'
    female='female'
    genders=[(male,'male'),(female,'female')]
    gender=forms.ChoiceField(required=True,choices=genders)
    class Meta:
        model=InsuranceApply
        fields=('profilepic','age','date_of_birth','state','country','city','income','phone','insurance_type','gender','nominee_name','nominee_address',) 

















class WorkerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model= Worker
        fields=['address','mobile','profile_pic']











