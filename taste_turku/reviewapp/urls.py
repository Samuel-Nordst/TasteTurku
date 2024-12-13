from django.urls import path
from . import views

app_name = 'reviewapp'
urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),
    path('restaurants/', views.restaurants, name='restaurants'),
]