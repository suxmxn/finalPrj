from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=30)  # 상품명
    content = models.TextField()    # 설명
    price = models.CharField(max_length=20) # 상품 가격
    maker = models.CharField(max_length=30) # 제조사
    made_at = models.DateTimeField()    # 제조년월
    color = models.CharField(max_length=20) # 컬러
    hook_text = models.CharField(max_length=100, blank=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product_image = models.ImageField(upload_to='shopping/images/%Y/%m/%d/', blank=True)  # 상품 이미지
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)  # 카테고리

    def __str__(self):
        return f'[{self.pk}]{self.name} :: {self.author}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}/'
