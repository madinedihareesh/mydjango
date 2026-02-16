from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RigistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),error_messages={'required':'Email required'})
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),error_messages={'required':'First name required'})
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),error_messages={'required':'Last Name required'})
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),error_messages={'required':'Password required'})
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}),error_messages={'required':'Password required'})
    class Meta:

        model = User
        fields = ['username','email','first_name','last_name']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))