from django.shortcuts import render
from .models import Product, Animal


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'store/animal_list.html', {'animals': animals})



