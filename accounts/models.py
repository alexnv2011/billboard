from django.db import models

# Create your models here.
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class CommonSignupForm(SignupForm):
    pass
