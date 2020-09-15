from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForms(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForms, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
