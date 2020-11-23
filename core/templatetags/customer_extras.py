from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString


register = Library()


@register.simple_tag
def customer_format(customer, short=False):
    if short:
        return f'{customer.company_name} ({customer.email})'
    return SafeString(f'<p><strong>{customer.company_name}</strong></p> email: {customer.email} NIP: {customer.NIP}')


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value} </p>')