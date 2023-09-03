from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        

class LoginForm(AuthenticationForm):
    class Meta:
        model = User