from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import redirect
from django.http import Http404


from .models import *
from .forms import *

# Create your views here.


def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated():
        username = request.user.username
        usereamil = request.user.email
        try:
            user = AuthUser.objects.get(username=username)
            diaries = Diary.objects.filter(user=user).order_by('-ddate')

        except:
            pass

    messages.get_messages(request)

    template = get_template('index.html')
    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(request_content)

    return HttpResponse(html)


def login(request):
    # next = request.GET.get('next')
    if request.method == 'POST':
        login_form = Login_form(request.POST)
        if login_form.is_valid():
            user_name = request.POST['username'].strip()
            user_password = request.POST['password']
            user = authenticate(username=user_name, password=user_password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '登陆成功')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '账号未启用')
            else:
                messages.add_message(request, messages.WARNING, '登录失败')
        else:
            messages.add_message(request, messages.INFO, '请检查您的字段')
    else:
        login_form = Login_form()


    template = get_template('login.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)


@login_required
def useinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            user = AuthUser.objects.get(username=username)
            useinfo = ProUser.objects.get(user=user)
        except:
            pass

    template = get_template('userinfo.html')
    html = template.render(locals())

    return HttpResponse(html)


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, '成功注销了！')
    return redirect('/')


@login_required
def posting(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)

    if request.method == 'POST':
        user = AuthUser.objects.get(username=username)
        print(user)
        diary = Diary(user=user)
        print(user, diary)
        post_form = DiaryForm(request.POST, instance=diary)
        print(post_form)
        if post_form.is_valid():
            post_form.save()
            messages.add_message(request, messages.SUCCESS, '日记发布成功')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, '如果需要发布日记，就需要把所有的字段都填写完！')
    else:
        post_form = DiaryForm()
        messages.add_message(request, messages.INFO, '如果您要张贴日记，需要把每个字段都填写完')

    template = get_template('posting.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(request_content)

    return HttpResponse(html)
