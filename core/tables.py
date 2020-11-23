from django_tables2 import tables

from core.models import DailyRoute


class DailyRouteTable(tables.Table):
    class Meta:
        model = DailyRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ("start", 'end', 'date', 'distance',)