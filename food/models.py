from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)
    rating = models.FloatField(default=4.0)
    price_range = models.CharField(max_length=50, default="₹200–₹400")

    def __str__(self):
        return self.name


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
