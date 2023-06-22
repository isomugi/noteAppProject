from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'conntent': '投稿内容',
        }

""" class LoginForm(forms.Form):
    username = forms.CharField(label = 'username')
    password = forms.CharField(label = 'password', widget = forms.PasswordInput) """

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')