# employees/templatetags/form_filters.py

from django import template

register = template.Library()

# Example simple tag
@register.simple_tag
def hello_tag():
    return "Hello from form_filters!"

# Example filter: uppercase a string
@register.filter(name='upper')
def upper(value):
    return value.upper()
