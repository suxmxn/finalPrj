from django.db import models
from django.contrib.auth.models import User
import os
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shopping/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shopping/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=30)  # 상품명
    content = MarkdownxField()    # 설명
    price = models.CharField(max_length=20) # 상품 가격
    maker = models.CharField(max_length=30) # 제조사
    made_at = models.DateTimeField()    # 제조년월
    color = models.CharField(max_length=20) # 컬러
    hook_text = models.CharField(max_length=100, blank=True)    #요약문

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  #작성자
    product_image = models.ImageField(upload_to='shopping/images/%Y/%m/%d/', blank=True)  # 상품 이미지

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)  # 카테고리
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.name} :: {self.author}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.content)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else :
            return 'https://doitdjango.com/avatar/id/391/b4bd3e4d86e66342/svg/{self.author.email}/'

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 어떤 상품에 대한 댓글인지
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    content = models.TextField()    # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)    # 작성일시
    modified_at = models.DateTimeField(auto_now=True)   # 수정일시

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else :
            return 'https://doitdjango.com/avatar/id/391/b4bd3e4d86e66342/svg/{self.author.email}/'
