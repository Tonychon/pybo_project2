import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

#템플릿 태그에서 사용하기위한 필터 (조건)을 만들어보자
@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))