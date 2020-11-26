from django.contrib.auth.mixins import LoginRequiredMixin
from slick_reporting.fields import SlickReportField
from slick_reporting.views import SlickReportView
from concurrent.futures._base import LOGGER
import django_tables2 as tables
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView, SingleTableMixin
from django_tables2.export import ExportMixin

from core.filters import DailyRouteFilter
from core.models import Employee, Customer, Order, Truck, DailyRoute
from core.forms import EmployeeForm, CustomerForm, OrderForm, TruckForm, DailyRouteForm
from core.tables import DailyRouteTable
from django.db.models import Sum


class EmployeeListView(LoginRequiredMixin, ListView):
    template_name = 'employees.html'
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_list'] = Employee.objects.all()
        return context


class CustomerListView(LoginRequiredMixin, ListView):
    template_name = 'customers.html'
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_list'] = Customer.objects.all()
        return context


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'orders.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.all()
        return context


class TruckListView(LoginRequiredMixin, ListView):
    template_name = 'trucks.html'
    model = Truck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['truck_list'] = Truck.objects.all()
        return context


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'employee_detail.html'
    model = Employee


class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'customer_detail.html'
    model = Customer


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = 'order_detail.html'
    model = Order


class TruckDetailView(LoginRequiredMixin, DetailView):
    template_name = 'truck_detail.html'
    model = Truck


class DailyRouteDetailView(LoginRequiredMixin, DetailView):
    template_name = 'daily_route_detail.html'
    model = DailyRoute


class EmployeeCreateView(LoginRequiredMixin, CreateView):
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


class CustomerCreateView(LoginRequiredMixin, CreateView):
    title = 'Add Customer'
    template_name = 'forms.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')


class OrderCreateView(LoginRequiredMixin, CreateView):
    title = 'Add Order'
    template_name = 'forms.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')


class TruckCreateView(LoginRequiredMixin, CreateView):
    title = 'Add Truck'
    template_name = 'forms.html'
    form_class = TruckForm
    success_url = reverse_lazy('truck_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class DailyRouteCreateView(LoginRequiredMixin, CreateView):
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


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
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


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    title = 'Update Customer'
    model = Customer
    template_name = 'forms.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    title = 'Update Order'
    model = Order
    template_name = 'forms.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class TruckUpdateView(LoginRequiredMixin, UpdateView):
    title = 'Update Truck Details'
    model = Truck
    template_name = 'forms.html'
    form_class = TruckForm
    success_url = reverse_lazy('truck_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class DailyRouteUpdateView(LoginRequiredMixin, UpdateView):
    title = 'Update Daily Route'
    model = DailyRoute
    template_name = 'forms.html'
    form_class = DailyRouteForm
    success_url = reverse_lazy('daily_routes')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    # form_class = MovieForm
    success_url = reverse_lazy('employee_list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')


class TruckDeleteView(LoginRequiredMixin, DeleteView):
    model = Truck
    template_name = 'truck_confirm_delete.html'
    success_url = reverse_lazy('truck_list')


class DailyRouteDeleteView(LoginRequiredMixin, DeleteView):
    model = DailyRoute
    template_name = 'daily_route_confirm_delete.html'
    success_url = reverse_lazy('daily_routes')


class DailyRouteListView(LoginRequiredMixin, ExportMixin, SingleTableView):
    model = DailyRoute
    table_class = DailyRouteTable
    template_name = 'daily_routes.html'


# class DailyRouteListView(ExportMixin, SingleTableView):
#     model = DailyRoute
#     table_class = DailyRouteTable
#     template_name = 'daily_routes.html'

class FilteredDailyRouteListView(LoginRequiredMixin, SingleTableMixin, ExportMixin, FilterView):
    table_class = DailyRouteTable
    model = DailyRoute
    template_name = "daily_routes.html"
    filterset_class = DailyRouteFilter


# class MonthlyDistanceTraveled(SlickReportView):
#     # The model where you have the data
#     report_model = DailyRoute
#     # template_name = "dashboard.html"
#     # the main date field used for the model.
#     date_field = 'date'
#     # or 'order__date_placed'
#     # this support traversing, like so
#     # date_field = 'order__date_placed'
#
#     # A foreign key to group calculation on
#     # group_by = 'end'
#     # time_series_pattern = 'monthly'
#     # time_series_columns = ['__total_distance__']
#     # The columns you want to display
#     columns = ['distance',
#         SlickReportField.create(Sum, 'distance', name='sum__distance'),
#         SlickReportField.create(Sum, 'fuel_consumed')]
#
#     # Charts
#     chart_settings = [
#      {
#         'type': 'bar',
#         'data_source': 'distance',
#         'title_source': 'title',
#         'title': 'Total Distance per Route',
#         'plot_total': True,
#      },
#     ]


class MonthlyDistanceTraveled(TemplateView):
    template_name = 'dashboard.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['qs'] = DailyRoute.objects.all()
    #     return context
