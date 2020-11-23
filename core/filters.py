import django_filters

from core.models import DailyRoute


class DailyRouteFilter(django_filters.FilterSet):
    class Meta:
        model = DailyRoute
        fields = ['start', 'end']