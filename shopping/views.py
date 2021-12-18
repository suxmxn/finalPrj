from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product, Category, Tag
from django.core.exceptions import PermissionDenied

class ProductList(ListView):
    model = Product
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_product_count'] = Product.objects.filter(category=None).count()
        return context

class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_product_count'] = Product.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        product_list = Product.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        product_list = Product.objects.filter(category=category)

    return render(request, 'shopping/product_list.html',
                  {
                      'product_list': product_list,
                      'categories': Category.objects.all(),
                      'no_category_product_count': Product.objects.filter(category=None).count(),
                      'category': category,
                  }
                  )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    product_list = tag.product_set.all()

    return render(request, 'shopping/product_list.html',
                  {
                      'product_list': product_list,
                      'tag': tag,
                      'categories': Category.objects.all(),
                      'no_category_product_count': Product.objects.filter(category=None).count(),
                  }
                  )

class ProductCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'hook_text', 'content', 'product_image', 'made_at', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(ProductCreate, self).form_valid(form)
        else:
            return redirect('/shopping/')

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'price', 'hook_text', 'content', 'product_image', 'made_at', 'category', 'tags']

    template_name = 'shopping/product_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(ProductUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied