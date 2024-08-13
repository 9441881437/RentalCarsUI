from django.db import models

# Create your models here.

class LoginModels(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 15)

class SignupModel(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 200)
    phone = models.BigIntegerField(max_length = 10)

class MainPage(models.Model):
    pass
