# app名/templatetags/myfun.py 文件

from django import template

register = template.Library()

@register.filter()
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})

@register.filter()
def widget_with_classes(value, arg):
    return value.as_widget(attrs={'class': arg})