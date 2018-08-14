from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.CharField(primary_key=True, max_length=20)
    pwd = models.CharField(max_length=20)
    email =models.EmailField(max_length=254,help_text='Enter valid email address.')

