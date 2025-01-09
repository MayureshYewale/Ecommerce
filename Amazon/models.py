from django.db import models

#Creating user models
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


#creating an product model
class Product(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    Description=models.TextField()
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    category=models.ForeignKey('category',on_delete=models.SET_NULL,null=True,related_name='Products')

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.Name 
    
#creating category model
class category(models.Model):
    name=models.CharField( max_length=250)
    Description=models.TextField(max_length=255,blank=True)
    parent_category=models.ForeignKey(
        'self',on_delete=models.SET_NULL,null=True,blank=True,related_name='subcategories'
    )
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_created=True)
    
    def __str__(self):
        return self.name
    

#creating order model 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    shipping_address = models.TextField()
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"


#creatinng orderitems model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.Name}"

#creating payment model
class Payment(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    payment_method = models.CharField(max_length=50)
    payment_reference = models.CharField(max_length=100, unique=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.status}"