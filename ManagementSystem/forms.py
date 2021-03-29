from django import forms
from django.forms import ModelForm, PasswordInput
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from .models import *

class RegistrationPage(forms.ModelForm):
    name= forms.CharField(max_length=150)
    emailId = forms.EmailField(label = 'Email Id')
    contactno = PhoneField()
    username = forms.CharField(min_length=4,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput,min_length=6,validators=[validate_password])
    confirmpassword = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = UserManagementSystem
        fields = "__all__"

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if UserManagementSystem.objects.filter(username=username).exists():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if UserManagementSystem.objects.filter(email=email).exists():
            raise  ValidationError("Email already exists")
        return email

    def clean(self):
        cleaned_data = super(RegistrationPage, self).clean()
        # This method will set the `cleaned_data` attribute
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("confirmpassword")
        if password != re_password:
            raise ValidationError("Passwords doesn't match")
        

class ClientInfoForm(forms.ModelForm):
    name= forms.CharField(max_length=150)
    emailId = forms.EmailField(label = 'Email Id')
    phno = PhoneField()
    clientid = forms.CharField(max_length = 50)
    address = forms.CharField(widget = forms.Textarea)
    
    class Meta:
        model = ClientManagementSystem
        fields = "__all__" 

class DeviceInfoForm(forms.Form):
    deviceid = forms.ModelChoiceField(queryset=ClientManagementSystem.objects.all())
    macaddress= forms.CharField(max_length=12)
    class Meta:
        model = DeviceInfo
        fields = ['macaddress','deviceid']


        
    