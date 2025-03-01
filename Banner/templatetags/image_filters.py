from django import template
import base64

register = template.Library()

@register.filter
def to_base64(value):
    if value:
        try:
            return base64.b64encode(value).decode('utf-8')
        except Exception as e:
            return f"Error encoding: {str(e)}"
    return ''