from django.contrib import admin
from Amazon.models import Product,category,User,Order,OrderItem,Payment
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'created_at')
    search_fields = ('email', 'name')
    list_filter = ('is_active',)

class ProductAdmin(admin.ModelAdmin):
    list_display=('Name','Description','Price')
    search_fields=('Name',)
    list_filter=('Name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','Description','parent_category')
    search_fields=('name',)
    list_filter=('name',)
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at')
    search_fields = ('user__email',)
    list_filter = ('created_at',)
    
class OrderitemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order__created_at',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'status', 'payment_method', 'payment_reference', 'transaction_date')
    list_filter = ('status', 'payment_method', 'transaction_date')
    search_fields = ('payment_reference', 'order__id', 'status')
    readonly_fields = ('transaction_date',)
    
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(category,CategoryAdmin)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderitemsAdmin)
admin.site.register(Payment,PaymentAdmin)

