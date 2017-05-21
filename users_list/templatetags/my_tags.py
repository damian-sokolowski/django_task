import datetime
from django import template

register = template.Library()


@register.simple_tag
def eligible(date):
    if date:
        age = (datetime.date.today() - date).days / 365
        if age < 13:
            return "blocked"
        else:
            return "allowed"

    return ""


@register.simple_tag
def bizzfuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "BizzFuzz"
    elif number % 3 == 0:
        return "Bizz"
    elif number % 5 == 0:
        return "Fuzz"
    return number

