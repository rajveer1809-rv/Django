from django.contrib import admin
from .models import (
    User, Customer, Vendor,
    Category, Product,
    Cart, CartItem,
    Order, OrderItem,
    Payment, Review
)

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Review)
