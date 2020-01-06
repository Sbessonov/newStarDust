from django.db import models

# Create your models here.
# первичный ключ создается автоматически id = models.AutoField()


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)