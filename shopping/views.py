from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductList(ListView):
    model = Product
    ordering = '-pk'

class ProductDetail(DetailView):
    model = Product
