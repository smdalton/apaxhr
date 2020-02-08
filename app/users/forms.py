from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import Employee

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = ('email',)
