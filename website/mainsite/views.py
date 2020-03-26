from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import redirect
from django.contrib import messages
from django.template import RequestContext
import datetime

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import *
from .forms import *
from logininfo.models import CustomUser
# Create your views here.



def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    all_poll = Poll.objects.all().order_by('-created_date')
    paginator = Paginator(all_poll, 5)
    p = request.GET.get('p')

    try:
        polls = paginator.page(p)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    template = get_template('mvote/index.html')

    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(request_content)

    return HttpResponse(html)

@login_required(login_url='/login')
def poll(request, pollid):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    try:
        poll = Poll.objects.get(id=pollid)
    except:
        poll = None

    if poll is not None:
        pollitems = PollItem.objects.filter(poll=poll).order_by('-vote')

    template = get_template('mvote/poll.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

@login_required(login_url='/login')
def vote(request, pollid, pollitemid):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    tar_url = '/mvote/poll/' + pollid
    if VoteCheck.objects.filter(userid=request.user.id,
                                pollid=pollid, vote_date=datetime.date.today()):
        messages.add_message(request, messages.WARNING, '一天只能投一票')
        return redirect(tar_url)
    else:
        vote_rec = VoteCheck(userid=request.user.id,
                             pollid=pollid, vote_date=datetime.date.today())
        vote_rec.save()

    try:
        pollitem = PollItem.objects.get(id=pollitemid)
    except:
        pollitem = None

    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()



    return redirect(tar_url)


@login_required(login_url='/login')
def addpoll(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        try:
            user = CustomUser.objects.get(username=username)
            polls = Poll.objects.filter(user=user)
        except:
            user = CustomUser(username=username)
    if request.method == 'POST':
        user = CustomUser.objects.get(username=username)
        poll = Poll(user=user)
        forms = PollForm(request.POST, instance=poll)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.INFO, '话题创建成功')
            return HttpResponseRedirect('.')
        else:
            messages.add_message(request, messages.WARNING, '需要填写话题标题')
    else:
        forms = PollForm()



    template = get_template('mvote/addpoll.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(context=locals(), request=request)

    return HttpResponse(html)

@login_required(login_url='/login')
def updatepollitem(request, pollid):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        try:
            poll = Poll.objects.get(id=pollid)
            pollitems = PollItem.objects.filter(poll=poll)
        except:
            poll = Poll(id=pollid)
    if request.method == 'POST':
        poll = Poll.objects.get(id=pollid)
        pollitem = PollItem(poll=poll)
        forms = PollItemForm(request.POST, instance=pollitem)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.INFO, '选项创建成功')
            return HttpResponseRedirect('/mvote/addpoll/' + str(pollid))
        else:
            messages.add_message(request, messages.WARNING, '至少需要填写选项')
    else:
        forms = PollItemForm()

    template = get_template('mvote/updatepollitem.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(context=locals(), request=request)

    return HttpResponse(html)

@login_required(login_url='/login')
def delpoll(request, pollid):
    try:
        poll = Poll.objects.get(id=pollid)
        poll.delete()
        return HttpResponseRedirect('/mvote/addpoll')
    except:
        return False

@login_required(login_url='/login')
def delpollitem(request, pollitemid):
    if request.method == 'GET' and request.is_ajax():
        try:
            pollitem = PollItem.objects.get(id=pollitemid)
            pollitem.delete()

            return HttpResponse('1')
        except:
            return HttpResponse('0')
    else:
        return HttpResponse('0')


@login_required(login_url='/login')
def govote(request):
    if request.method == 'GET' and request.is_ajax():
        pollitemid = request.GET.get('pollitemid')
        pollid = request.GET.get('pollid')
        bypass = False
        votes = 0
        if VoteCheck.objects.filter(userid=request.user.id,
                                    pollid=pollid, vote_date=datetime.date.today()):
            bypass = True
            return HttpResponse(votes)
        else:
            vote_rec = VoteCheck(userid=request.user.id,
                             pollid=pollid, vote_date=datetime.date.today())
            vote_rec.save()
        try:
            pollitem = PollItem.objects.get(id=pollitemid)
            if not bypass:
                pollitem.vote += 1
                pollitem.save()
            votes = pollitem.vote
        except:
            votes = 0
    else:
        votes = 0
    return HttpResponse(votes)