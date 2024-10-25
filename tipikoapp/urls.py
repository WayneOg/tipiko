from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('events/', views.events, name='events'),
    path('market/', views.market, name='market'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('shop/', views.shop, name='shop'),
    path('regions/', views.regions, name='regions'),
]
