from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.f_name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_summa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total_qty = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self) -> str:
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=255)
<<<<<<< HEAD
    img = models.ImageField(upload_to='watches-img/')
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
=======
    img = models.ImageField(upload_to='images/')
>>>>>>> 67deb43ece3e734db73ed23888567b8c2e9c3b75

    def __str__(self) -> str:
        return self.title

<<<<<<< HEAD
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    watch = models.ForeignKey(Watches, on_delete=models.CASCADE)
    body = models.TextField()
=======

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    color = models.CharField(max_length=100)
    count = models.DecimalField(max_digits=5, decimal_places=2, null=True )
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
>>>>>>> 67deb43ece3e734db73ed23888567b8c2e9c3b75

    def __str__(self) -> str:
        return self.title


class Cart_product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    summa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.title


class Comment(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text