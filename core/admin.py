from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import Customer, Truck, Employee, Order, Post, DailyRoute
from django.contrib.auth.models import User

admin.site.register(Customer)
admin.site.register(Truck)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Post)
admin.site.register(DailyRoute)

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)