from django.shortcuts import render
from .models import Restaurant

def index(request):
    return render(request, 'reviewapp/index.html')

def restaurants(request):
    restaurants  = Restaurant.objects.order_by('date_added')
    context = {'restautants': restaurants}
    return render(request, 'reviewapp/restaurants.html', context)

# Create your views here.
