from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Todolist
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class TodoForm(forms.ModelForm):
    
    class Meta:
        model=Todolist
        fields=['title','description','completed']
        

