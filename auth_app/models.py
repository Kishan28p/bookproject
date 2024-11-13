from django.db import models

# Create your models here.


class UserRegistration(models.Model):
    full_name =models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    cpassword = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)



class LoginTable(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)

