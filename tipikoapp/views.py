from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index2.html')

def events(request):
    return render(request, 'events.html')


def restaurant(request):
    return render(request, 'restaurant.html')

def market(request):
    return render(request, 'market.html')

def regions(request):
    return render(request, 'regions.html')


def shop(request):
    return render(request, 'shop.html')
