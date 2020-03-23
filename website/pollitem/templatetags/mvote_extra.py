from django import template
from pollitem import models

register = template.Library()

@register.filter(name='show_items')
def show_items(values):
    try:
        poll = models.Poll.objects.get(id=int(values))
        items = models.PollItem.objects.filter(poll=poll).count()
    except:
        items = 0

    return items

@register.filter(name='show_votes')
def show_votes(values):
    try:
        poll = models.Poll.objects.get(id=int(values))
        pollitems = models.PollItem.objects.filter(poll=poll)
        votes = 0
        for pollitem in pollitems:
            votes = pollitem.vote + votes
    except:
        votes = 0

    return votes