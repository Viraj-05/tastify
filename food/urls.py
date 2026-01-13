from django.urls import path
from .views import (
    home, restaurant_detail, order_food, login_view, logout_view,
    add_to_cart, view_cart, order_history
)

urlpatterns = [
    path('', home, name='home'),
    path('restaurant/<int:restaurant_id>/', restaurant_detail, name='restaurant_detail'),
    path('order/<int:restaurant_id>/', order_food, name='order'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cart/', view_cart, name='cart'),
    path('cart/add/<int:restaurant_id>/', add_to_cart, name='add_to_cart'),
    path('orders/', order_history, name='order_history'),
]
