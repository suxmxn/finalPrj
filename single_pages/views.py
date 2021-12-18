from django.shortcuts import render
from shopping.models import Product

def landing(request):
    recent_products = Product.objects.order_by('-pk')[:3]
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_products': recent_products,
        }
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

def about_company(request):
    return render(
        request,
        'single_pages/about_company.html'
    )
