from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Restaurant, Order


def home(request):
    query = request.GET.get('search')

    if query:
        restaurant_list = Restaurant.objects.filter(name__icontains=query)
    else:
        restaurant_list = Restaurant.objects.all()

    paginator = Paginator(restaurant_list, 8)
    page_number = request.GET.get('page')
    restaurants = paginator.get_page(page_number)

    return render(request, 'food/home.html', {
        'restaurants': restaurants,
        'query': query
    })


def order_food(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    Order.objects.create(restaurant=restaurant)

    return render(request, 'food/order_success.html', {
        'restaurant': restaurant
    })
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'food/restaurant_detail.html', {
        'restaurant': restaurant
    })
def order_history(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'food/order_history.html', {
        'orders': orders
    })
