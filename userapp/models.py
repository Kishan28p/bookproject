# from tkinter.constants import CASCADE

from django.db import models
from django.db.models import CASCADE

from auth_app.models import LoginTable, UserRegistration

from bookapp.models import Book


# Create your models here.


class Cart(models.Model):
    user=models.OneToOneField(LoginTable,on_delete=CASCADE)
    items=models.ManyToManyField(Book)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=CASCADE)
    book=models.ForeignKey(Book,on_delete=CASCADE)
    quantity=models.PositiveIntegerField(default=1)