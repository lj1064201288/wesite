from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from django.contrib import messages
from django.template import RequestContext

from .models import *
# Create your views here.



def index(request):
    polls = Poll.objects.all()
    template = get_template('index.html')

    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(request_content)

    return HttpResponse(html)


def poll(request, pollid):
    try:
        poll = Poll.objects.get(id=pollid)
    except:
        poll = None

    if poll is not None:
        pollitems = PollItem.objects.filter(poll=poll).order_by('-vote')

    template = get_template('poll.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

def vote(request, pollid, pollitemid):

    try:
        pollitem = PollItem.objects.get(id=pollitemid)
    except:
        pollitem = None
    if int(pollitemid) != 1:
        messages.add_message(request, messages.WARNING, '投票错误，请重新选择!')
        return redirect('/poll/' + pollid)
    else:
        messages.add_message(request, messages.SUCCESS, '投票成功，英雄所见略同.')
    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()

    tar_url = '/poll/' + pollid

    return redirect(tar_url)
