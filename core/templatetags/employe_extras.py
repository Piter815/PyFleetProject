from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString


register = Library()


@register.simple_tag
def employee_format(employee, short=False):
    if short:
        return f'{employee.name} ({employee.surname})'
    return f'{employee.title} ({employee.released.year}) {employee.genre}'


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value} </p>')