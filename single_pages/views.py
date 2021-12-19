from django.shortcuts import render
from shopping.models import Product, Comment, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin



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
    comments = Comment.objects.all()
    return render(
        request,
        'single_pages/about_me.html',
        {
            'comments': comments,
        }
    )

def about_company(request):
    category = Category.objects.all()
    tag = Tag.objects.all()
    return render(
        request,
        'single_pages/about_company.html',
        {
            'category': category,
            'tag': tag,
        }
    )
