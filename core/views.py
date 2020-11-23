from concurrent.futures._base import LOGGER
import django_tables2 as tables
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from core.models import Employee, Customer, Order, Truck, DailyRoute
from core.forms import EmployeeForm, CustomerForm, OrderForm, TruckForm, DailyRouteForm
from core.tables import DailyRouteTable


class EmployeeListView(ListView):
    template_name = 'employees.html'
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_list'] = Employee.objects.all()
        return context


class CustomerListView(ListView):
    template_name = 'customers.html'
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_list'] = Customer.objects.all()
        return context


class OrderListView(ListView):
    template_name = 'orders.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.all()
        return context

class TruckListView(ListView):
    template_name = 'trucks.html'
    model = Truck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['truck_list'] = Truck.objects.all()
        return context


class EmployeeDetailView(DetailView):
    template_name = 'employee_detail.html'
    model = Employee


class CustomerDetailView(DetailView):
    template_name = 'customer_detail.html'
    model = Customer


class OrderDetailView(DetailView):
    template_name = 'order_detail.html'
    model = Order


class TruckDetailView(DetailView):
    template_name = 'truck_detail.html'
    model = Truck


class DailyRouteDetailView(DetailView):
    template_name = 'daily_route_detail.html'
    model = DailyRoute


class EmployeeCreateView(CreateView):
    title = 'Add Employee'
    template_name = 'forms.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_create')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class CustomerCreateView(EmployeeCreateView):
    title = 'Add Customer'
    template_name = 'forms.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')


class OrderCreateView(EmployeeCreateView):
    title = 'Add Order'
    template_name = 'forms.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

class TruckCreateView(CreateView):
    title = 'Add Truck'
    template_name = 'forms.html'
    form_class = TruckForm
    success_url = reverse_lazy('trucks_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class DailyRouteCreateView(CreateView):
    title = 'Add Daily Route'
    template_name = 'forms.html'
    form_class = DailyRouteForm
    success_url = reverse_lazy('daily_routes')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class EmployeeUpdateView(UpdateView):
    title = 'Update Employee'
    model = Employee
    template_name = 'forms.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_list')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class CustomerUpdateView(UpdateView):
    title = 'Update Customer'
    model = Customer
    template_name = 'forms.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class OrderUpdateView(UpdateView):
    title = 'Update Order'
    model = Order
    template_name = 'forms.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class TruckUpdateView(UpdateView):
    title = 'Update Truck Details'
    model = Truck
    template_name = 'forms.html'
    form_class = TruckForm
    success_url = reverse_lazy('truck_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class DailyRouteUpdateView(UpdateView):
    title = 'Update Daily Route'
    model = DailyRoute
    template_name = 'forms.html'
    form_class = DailyRouteForm
    success_url = reverse_lazy('daily_routes')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    # form_class = MovieForm
    success_url = reverse_lazy('employee_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')


class TruckDeleteView(DeleteView):
    model = Truck
    template_name = 'truck_confirm_delete.html'
    success_url = reverse_lazy('truck_list')


class DailyRouteDeleteView(DeleteView):
    model = DailyRoute
    template_name = 'daily_route_confirm_delete.html'
    success_url = reverse_lazy('daily_routes')


class DailyRouteListView(SingleTableView):
    model = DailyRoute
    table_class = DailyRouteTable
    template_name = 'daily_routes.html'
