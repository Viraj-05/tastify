from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)
    rating = models.FloatField(default=4.0)
    price_range = models.CharField(max_length=50, default="₹200–₹400")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"

class FoodItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='items'
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
