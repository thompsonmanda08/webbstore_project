from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from .forms import RegisterForm


# Create your views here.
# CRUD - 1. Create  2. Read(Retrieve)  3. Update  4. Delete
# CRUD - R = Reading

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'products.html', context)


def product_details(request, prod_id):
    product = Product.objects.get(id=prod_id)
    context = {'product': product}

    return render(request, 'product_details.html', context)

# CRUD  - C = Create
# Creating a new product in the Database from the Frontend
def register_product(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products')

    context = {
        'form': form,
        'form_type': 'REGISTER'
    }
    return render(request, 'register_product.html', context)


# CRUD - U = Update
# Updating an existing product from the Frontend
def update_product(request, prod_id):
    product = Product.objects.get(id=prod_id)
    form = RegisterForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products')

    context = {
        'form': form,
        'form_type': 'UPDATE'
    }

    return render(request, 'register_product.html', context)


# CRUD - D = Delete
# Deleting a product from the Frontend

def delete_product(request, prod_id):
    product = Product.objects.get(id=prod_id)
    product.delete()

    return HttpResponseRedirect('/products')

