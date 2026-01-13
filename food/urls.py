from django.urls import path
from .views import home, order_food, restaurant_detail, order_history

urlpatterns = [
    path('', home, name='home'),
    path('order/<int:restaurant_id>/', order_food, name='order'),
    path('restaurant/<int:restaurant_id>/', restaurant_detail, name='restaurant_detail'),
    path('orders/', order_history, name='order_history'),

]
