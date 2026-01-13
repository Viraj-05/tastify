from django.contrib import admin
from .models import Restaurant, FoodItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "restaurant")
    list_filter = ("restaurant",)
    search_fields = ("name",)
