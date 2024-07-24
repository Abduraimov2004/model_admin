from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self) -> str:
        return self.username





class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=50)
    count = models.PositiveSmallIntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    total_summa = models.DecimalField(max_digits=5, decimal_places=2)
    total_qty = models.PositiveSmallIntegerField(default=0)



class Cart_Product(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.PositiveSmallIntegerField(default=0)
    summa = models.DecimalField(max_digits=5, decimal_places=2)



class Comment(models.Model):
    text = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
