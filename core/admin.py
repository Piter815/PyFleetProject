from django.contrib import admin

from core.models import Customer, Truck, Employee, Order, Post, DailyRoute

admin.site.register(Customer)
admin.site.register(Truck)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Post)
admin.site.register(DailyRoute)

