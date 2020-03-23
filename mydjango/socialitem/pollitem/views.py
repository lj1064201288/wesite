from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages

import datetime
from .models import *
from .forms import *
# Create your views here.

def index(request):
    all_polls = Poll.objects.all().order_by('-created_at')
    pageinator = Paginator(all_polls, 5)
    p = request.GET.get('page')

    try:
        polls = pageinator.page(p)
    except PageNotAnInteger:
        polls = pageinator.page(1)
    except EmptyPage:
        polls = pageinator.page(pageinator.num_pages)

    template = get_template('index.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

@login_required
def addpoll(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        user = User.objects.get(username=username)
        polls = Poll.objects.filter(user=user).order_by('-created_at')
    if request.method == 'POST':
        try:
            poll = Poll(user=user)
            forms = PollForm(request.POST, instance=poll)
            if forms.is_valid():
                forms.save()
                messages.add_message(request, messages.SUCCESS, '话题添加成功!')
                return redirect('.')
            else:
                messages.add_message(request, messages.WARNING, '添加失败，每个字段都是需要填写的')
        except:
            forms = PollForm()
            messages.add_message(request, messages.INFO, '发布话题~')
    else:
        forms = PollForm()


    template = get_template('addpoll.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

@login_required
def poll(request, pollid):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    try:
        user = User.objects.get(username=username)
    except:
        pass
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

@login_required
def vote(request, pollid, vodeid):
    tar_url = '/poll/' + pollid
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    if VoteCheck.objects.filter(userid=request.user.id, pollid=pollid, vote_time=datetime.date.today()):
        return redirect(tar_url)
    else:
        rec_vote = VoteCheck(userid=request.user.id, pollid=pollid, vote_time=datetime.date.today())
        rec_vote.save()

    try:
        pollitem = PollItem.objects.get(id=vodeid)
        messages.add_message(request,messages.SUCCESS, '投票成功~')
    except:
        pollitem = None

    if pollitem is not None:
        pollitem.vote += 1
        pollitem.save()

    return redirect(tar_url)

@login_required
def updatepollitem(request, pollid=None):
    path = request.path
    poll = Poll.objects.get(id=pollid)
    pollitems = PollItem.objects.filter(poll=poll)
    try:
        if request.method == 'POST':
            pollitem = PollItem(poll=poll)
            form = PollitemForm(request.POST, instance=pollitem)
            if form.is_valid():
                messages.add_message(request, messages.SUCCESS, '添加选项成功~')
                form.save()
                return redirect(path)
        else:
            form = PollitemForm()
            messages.add_message(request, messages.INFO, '上方填入选项信息')
    except:
        form = PollitemForm()
        messages.add_message(request, messages.WARNING, '没有找到该话题')
        return redirect('/addpoll')

    template = get_template('updatepollitem.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)

@login_required
def govote(request):
    if request.method == 'GET' and request.is_ajax():
        pollitemid = request.GET.get('pollitemid')
        pollid = request.GET.get('pollid')
        bypass = False
        if VoteCheck.objects.filter(userid=request.user.id, pollid=pollid, vote_time=datetime.date.today()):
            bypass = True
            messages.add_message(request, messages.WARNING, '一天只能投票一次.')
        else:
            rec_vote = VoteCheck(userid=request.user.id, pollid=pollid, vote_time=datetime.date.today())
            rec_vote.save()

        try:
            if not bypass:
                pollitem = PollItem.objects.get(id=pollitemid)
                pollitem.vote = pollitem.vote + 1
                pollitem.save()
            votes = pollitem.vote
        except:
            votes = 0
    else:
        votes = 0

    return HttpResponse(votes)
