from django import template
register = template.Library()

@register.filter
def vnd(value):
    try:
        amount = int(value)
    except (ValueError, TypeError):
        return value
    s = f"{amount:,}".replace(",", ".")
    return f"{s} VND"
