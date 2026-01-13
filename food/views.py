from django.shortcuts import render

def home(request):
    restaurants = [
        {"name": "China Point", "cuisine": "Indian, Chinese, Korean"},
        {"name": "Mba Bhurji", "cuisine": "Fast Food ,Egg Dishes"},
        {"name": "Lets Shawarma", "cuisine": "Afghani,Indian,Middle Eastern"},
        {"name": "Rolex Bakery", "cuisine": "Bakery Products"},
        {"name": "Cafe Durga", "cuisine": "Cafe, Beverages"},
        {"name": "Hotel Gajanan", "cusine": "Indian"},
        {"name": "Hotel Someshwar", "cuisine": "Daily mess"},
        {"name": "Cafe Mountain Dragon", "cuisine": "Ice cream,Cold and Hot Beverages"},
       
       
       
       
    ]
    query = request.GET.get('search')

    if query:
        restaurants = [
            r for r in restaurants
            if query.lower() in r["name"].lower()
        ]

    return render(request, 'index.html', {
        'restaurants': restaurants,
        'query': query
    })

