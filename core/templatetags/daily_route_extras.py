from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString


register = Library()


@register.simple_tag
def daily_route_format(daily_route, short=False):
    if short:
        return f'{daily_route.date} ({daily_route.truck})'
    return SafeString(f'<p><strong>Date: {daily_route.date}</strong></p> Driver: {daily_route.driver} Truck: {daily_route.truck}')


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value} </p>')