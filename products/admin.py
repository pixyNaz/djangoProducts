from django.contrib import admin
from products.models import Product, Comment

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'created_date', 'modified_date')
    sortable_by = ('rate',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)