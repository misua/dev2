from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User

from django import forms
from  django.forms.widgets import PasswordInput, TextInput





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



#uncomment this for the working code
class LoginForm(AuthenticationForm):
    
   username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

   class Meta:
       fields = ('username', 'password')
 
