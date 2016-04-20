from django import forms
from django.contrib.auth.models import User
from student.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password', 'username')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('enrol',)
