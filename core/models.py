from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.utils.datetime_safe import date


class Customer(models.Model):
    # customer_id = models.IntegerField()
    company_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    NIP = models.CharField(max_length=20, unique=True)
    billing_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.company_name}'


class Truck(models.Model):
    TYPE = (
        ('LOR', 'Lorry'),
        ('TRA', 'Tractor'),
        ('CIS', 'Cistern'),
        ('CON', 'Container'),
    )
    AVAILABILITY = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    # truck_id = models.IntegerField()
    model_name = models.CharField(max_length=40)
    production_date = models.DateField(null=True, blank=True, default=date.today)
    company_registration_date = models.DateField(null=True, blank=True, default=date.today)
    vin = models.CharField(max_length=40)
    reg_number = models.CharField(max_length=40)
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
    odometer = models.IntegerField(null=True, blank=True)
    service_interval = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=3, choices=TYPE)
    max_load = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=200)

    def __str__(self):
        return f'{self.model_name} Registered as: {self.reg_number}'


class Order(models.Model):
    ROUTETYPE = (
        ('KM', 'Distance'),
        ('TN', 'Weight'),
    )
    LOADTYPE = (
        ('MS', 'Dry mass'),
        ('LI', 'Liquid'),
        ('CO', 'Container'),
    )
    STATUS = (
        ('OP', 'Open'),
        ('CL', 'Closed'),
    )
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(default=date.today)
    route_type = models.CharField(max_length=2, choices=ROUTETYPE)
    load_type = models.CharField(max_length=2, choices=LOADTYPE)
    status = models.CharField(max_length=2, choices=STATUS)
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    truck = models.ManyToManyField(Truck)

    def __str__(self):
        return f'{self.order_id} for {self.customer}'


class Employee(models.Model):
    ROLE = (
        ('AD', 'Administration'),
        ('DR', 'Driver'),
    )
    AVAILABILITY = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    role = models.CharField(max_length=2, choices=ROLE)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    birth_date = models.DateField(default=date.today)
    billing_address = models.TextField(null=True, blank=True, max_length=200)
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
    qualifications = models.TextField(null=True, blank=True, max_length=200)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.role}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(Employee, on_delete=CASCADE)

    def __str__(self):
        return f'Post {self.title} by {self.author}'


class DailyRoute(models.Model):
    distance = models.IntegerField(null=True, blank=True)
    fuel_consumed = models.IntegerField(null=True, blank=True)
    start = models.CharField(max_length=40, null=True, blank=True)
    end = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateField(default=date.today)
    driver = models.ForeignKey(Employee, on_delete=CASCADE)
    truck = models.ForeignKey(Truck, on_delete=CASCADE)
    order = models.ForeignKey(Order, on_delete=CASCADE)

    def __str__(self):
        return f'Post {self.start} to {self.end} on {self.date}'