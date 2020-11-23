import django_tables2 as tables
from core.models import DailyRoute


ACTIONS = '''
   <a href="{% url 'daily_route_update' record.pk %}">Edit</a>
   <a href="{% url 'daily_route_detail' record.pk %}">View</a>
'''

class DailyRouteTable(tables.Table):
    actions = tables.TemplateColumn(ACTIONS)


    class Meta:
        model = DailyRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ('date', "start", 'end', 'distance', 'driver', 'truck', 'order',)