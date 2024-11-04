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

def contact(request):
    return render(request, 'contact.html')

def invest(request):
    return render(request, 'investors.html')

def shop(request):
    return render(request, 'shop.html')

def blog(request):
    return render(request, 'blog.html')
