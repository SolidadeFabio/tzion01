from django import template

register = template.Library()

@register.filter(name='replace_comma')
def replace_comma(value):
    value = str(value)
    return value.replace(',', '.')
