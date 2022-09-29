
from email import message
from tabnanny import verbose
from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length = 30, verbose_name = "Name")
    email = models.EmailField(verbose_name = "Email")
    address = models.CharField(max_length = 100, verbose_name = "Address")
    messages = models.TextField(verbose_name = "Messages")



