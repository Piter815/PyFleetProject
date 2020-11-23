from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit
from django import forms
from datetime import date
from core.models import Employee, Customer, Order
from django.core.exceptions import ValidationError


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('name'), Column('surname'), Column('role')),
            'salary',
            'birth_date',
            'qualifications',
            'phone',
            'email',
            'availability',
            'address',
            Submit('submit','Submit'),
        )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('company_name'), Column('email'), Column('phone')),
            'NIP',
            'billing_address',
            Submit('submit','Submit'),
        )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('order_id'), Column('order_date'), Column('customer')),
            'route_type',
            'load_type',
            'truck',
            'status',
            Submit('submit','Submit'),
        )