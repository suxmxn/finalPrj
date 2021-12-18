from django.contrib import admin
from .models import Product, Category, Tag, Comment
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Product, MarkdownxModelAdmin)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)