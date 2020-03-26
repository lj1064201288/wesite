from django import template
from mainsite import models

register = template.Library()

@register.filter(name='show_items')
def show_items(values):
    print(values)
    try:
        poll = models.Poll.objects.get(id=int(values))
        items = models.PollItem.objects.filter(poll=poll).count()
    except:
        print(values)
        items = 0
    return items

@register.filter(name='show_votes')
def show_votes(values):

    print('asfasfa')
    try:
        poll = models.Poll.objects.get(id=int(values))
        pollitems = models.PollItem.objects.filter(poll=poll)
        votes = 0
        for pollitem in pollitems:
            votes = pollitem.vote + votes
    except:
        print(values)
        votes = 0

    return votes


