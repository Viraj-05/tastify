from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Restaurant, Order, CartItem ,MenuItem
from django.shortcuts import redirect



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

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'food/restaurant_detail.html', {'restaurant': restaurant})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'food/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def order_food(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    Order.objects.create(user=request.user,restaurant=restaurant)
    return render(request, 'food/order_success.html', {'restaurant': restaurant})

@login_required(login_url='login')
def add_to_cart(request, item_id):
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='login')
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'food/cart.html', {'items': items})

@login_required(login_url='login')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'food/order_history.html', {'orders': orders})

@login_required(login_url='login')
def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = restaurant.menu_items.all()

    return render(request, 'food/menu.html', {
        'restaurant': restaurant,
        'menu_items': menu_items
    })


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'food/profile.html')


