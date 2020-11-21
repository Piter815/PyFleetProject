from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Employee


class EmployeeListView(ListView):
    template_name = 'employees.html'
    model = Employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_list'] = Employee.objects.all()
        return context


class EmployeeDetailView(DetailView):
    template_name = 'employee_detail.html'
    model = Employee


class TruckListView(ListView):
    template_name = 'trucks.html'
    model = Truck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['truck_list'] = Truck.objects.all()
        return context
