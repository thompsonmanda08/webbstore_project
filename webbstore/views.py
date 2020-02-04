from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'index.html', context)


def new(request):
    return HttpResponse("New Products")


def trending(request):
    return HttpResponse("Trending Products")
