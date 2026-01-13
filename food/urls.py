from django.urls import path
from .views import restaurant_menu
from food import views
from .views import (
    home, restaurant_detail, order_food, login_view, logout_view,
    add_to_cart, view_cart, order_history, restaurant_menu
)

urlpatterns = [
    path('', home, name='home'),
    path('restaurant/<int:restaurant_id>/menu/', restaurant_menu, name='menu'),
    path('order/<int:restaurant_id>/', order_food, name='order'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cart/', view_cart, name='cart'),
    path('cart/add/<int:restaurant_id>/', add_to_cart, name='add_to_cart'),
    path('orders/', order_history, name='order_history'),
    path('restaurant/<int:restaurant_id>/menu/', views.restaurant_menu, name='restaurant_menu'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]
