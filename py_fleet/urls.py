"""py_fleet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core.views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, \
    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView, OrderListView, \
    OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView
from py_fleet.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("core/", include('core.urls', namespace='core')),
    path("employee/list", EmployeeListView.as_view(), name='employee_list'),
    path("", IndexView.as_view(), name='index'),
    path("employee/detail/<pk>", EmployeeDetailView.as_view(), name="employee_detail"),
    path("employee/create", EmployeeCreateView.as_view(), name="employee_create"),
    path("employee/update/<pk>", EmployeeUpdateView.as_view(), name="employee_update"),
    path("employee/delete/<pk>", EmployeeDeleteView.as_view(), name="employee_delete"),
    path("customer/list", CustomerListView.as_view(), name='customer_list'),
    path("customer/detail/<pk>", CustomerDetailView.as_view(), name="customer_detail"),
    path("customer/create", CustomerCreateView.as_view(), name="customer_create"),
    path("customer/update/<pk>", CustomerUpdateView.as_view(), name="customer_update"),
    path("customer/delete/<pk>", CustomerDeleteView.as_view(), name="customer_delete"),
    path("order/list", OrderListView.as_view(), name='order_list'),
    path("order/detail/<pk>", OrderDetailView.as_view(), name="order_detail"),
    path("order/create", OrderCreateView.as_view(), name="order_create"),
    path("order/update/<pk>", OrderUpdateView.as_view(), name="order_update"),
    path("order/delete/<pk>", OrderDeleteView.as_view(), name="order_delete"),
]

