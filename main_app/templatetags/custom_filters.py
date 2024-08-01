from django import template

register = template.Library()

@register.filter
def to_range(value):
    return range(1, value + 1)

@register.filter
def dict_key(d, key):
    return d.get(key, [])

