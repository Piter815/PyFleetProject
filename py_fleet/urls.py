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



from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, \
    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView, OrderListView, \
    OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView, DailyRouteListView, DailyRouteDetailView, \
    DailyRouteCreateView, DailyRouteUpdateView, DailyRouteDeleteView, TruckDeleteView, TruckUpdateView, TruckCreateView, \
    TruckDetailView, TruckListView, FilteredDailyRouteListView, MonthlyDistanceTraveled
from blog.views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, HomeListView, PostListView
from py_fleet.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("core/", include('core.urls', namespace='core')),
    path("blog/", include('blog.urls', namespace='blog')),
    path("employee/list", EmployeeListView.as_view(), name='employee_list'),
    path("", HomeListView.as_view(), name='index'),
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
    path("daily-routes/list", FilteredDailyRouteListView.as_view(), name='daily_routes'),
    path("daily-routes/detail/<pk>", DailyRouteDetailView.as_view(), name="daily_route_detail"),
    path("daily-routes/create", DailyRouteCreateView.as_view(), name="daily_route_create"),
    path("daily-routes/update/<pk>", DailyRouteUpdateView.as_view(), name="daily_route_update"),
    path("daily-routes/delete/<pk>", DailyRouteDeleteView.as_view(), name="daily_route_delete"),
    path("truck/list", TruckListView.as_view(), name='truck_list'),
    path("truck/detail/<pk>", TruckDetailView.as_view(), name="truck_detail"),
    path("truck/create", TruckCreateView.as_view(), name="truck_create"),
    path("truck/update/<pk>", TruckUpdateView.as_view(), name="truck_update"),
    path("truck/delete/<pk>", TruckDeleteView.as_view(), name="truck_delete"),
    path("post/detail/<pk>", PostDetailView.as_view(), name="post_detail"),
    path("post/create", PostCreateView.as_view(), name="post_create"),
    path("post/update/<pk>", PostUpdateView.as_view(), name="post_update"),
    path("post/delete/<pk>", PostDeleteView.as_view(), name="post_delete"),
    path("post/list", PostListView.as_view(), name="post_list"),
    path("dashboard/", MonthlyDistanceTraveled.as_view(), name="dashboard"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)