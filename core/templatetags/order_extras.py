from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString


register = Library()


@register.simple_tag
def order_format(order, short=False):
    if short:
        return f'Order:{order.order_id} ({order.customer})'
    return SafeString(f'<p><strong>Order:{order.order_id}</strong></p> for: {order.customer} from: {order.order_date}')


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value} </p>')

