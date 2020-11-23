from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString


register = Library()


@register.simple_tag
def truck_format(truck, short=False):
    if short:
        return f'{truck.company_name} ({truck.email})'
    return SafeString(f'<p><strong>{truck.model_name}</strong></p> Year: {truck.production_date} Registration: {truck.reg_number}')


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value} </p>')