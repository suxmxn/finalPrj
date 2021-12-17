from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)  # 상품명
    content = models.TextField()    # 설명
    price = models.CharField(max_length=20) # 상품 가격
    maker = models.CharField(max_length=30) # 제조사
    made_at = models.DateTimeField()    # 제조년월
    color = models.CharField(max_length=20) # 컬러
    hook_text = models.CharField(max_length=100, blank=True)

    product_image = models.ImageField(upload_to='shopping/images/%Y/%m/%d/', blank=True)  # 상품 이미지
    # category  # 카테고리

    def __str__(self):
        return f'[{self.pk}]{self.name}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}/'
