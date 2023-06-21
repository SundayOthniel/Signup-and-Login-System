from django.db import models
from django.core.validators import MinLengthValidator

class SignUp(models.Model):
    surename = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=20)

