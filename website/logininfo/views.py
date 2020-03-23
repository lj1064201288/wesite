from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import datetime
import hashlib

from .models import *
from .forms import *
# Create your views here.


def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        try:
            nickname = CustomUser.objects.get(username=username).nickname
        except Exception:
            nickname = None
        try:
            user = CustomUser.objects.get(username=username)
            diaries = Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass


    messages.get_messages(request)
    template = get_template('logininfo/index.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(context=locals(), request=request)

    return HttpResponse(html)

def listing(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    template = get_template('logininfo/listing.html')
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = Mood.objects.all()

    html = template.render(locals())

    return HttpResponse(html)

@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    if request.method == 'POST':
        user = CustomUser.objects.get(username=username)
        diary = Diary(user=user)
        post_form = DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, '日记已添加')
            post_form.save()
            return HttpResponseRedirect('/diary')
        else:
            messages.add_message(request, messages.WARNING, '如果你要添加日记，需要每一个字段都正确填写')
    else:
        post_form = DiaryForm()
        messages.add_message(request, messages.WARNING, '如果你要添加日记，需要每一个字段都正确填写')

    template = get_template('logininfo/posting.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(context=locals(), request=request)

    return HttpResponse(html)


def contact(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = '感谢您的来信.'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            email_body = u'''
                网友姓名:{}
                居住城市:{}
                是否在校:{}
                反应如下：{}
            '''.format(user_name, user_city, user_school, user_message)

            email = EmailMessage('来自【进阶之路】的网友邮件', email_body, user_email, ['1064201288@qq.com'])

        else:
            message = '请正确填写内容'
    else:
        form = ContactForm()

    template = get_template('logininfo/contact.html')
    forms = ContactForm()
    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(context=locals(), request=request)

    return HttpResponse(html)

def post2db(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        print(post_form['mood'])
        if post_form.is_valid():
            message = '发布成功，不过需要等待管理员查看后才能正常发布!'
            post_form.save()
            return HttpResponseRedirect('/diary/list/')

        else:
            message = '如果您需要张贴，需要每个字段都要填写...'

    else:
        post_form = PostForm()
        message = '如果您要张贴，需要每个字段都要填写'

    template = get_template('logininfo/post2db.html')
    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(context=locals(), request=request)

    return HttpResponse(html)

def login(request):
    if request.method == 'POST':
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    hours = datetime.datetime.now().timetuple().tm_hour
                    if int(hours) < 11:
                        send = '早上好'
                    elif int(hours) >= 11 and hours < 14:
                        send = '中午好'
                    elif int(hours) >= 14 and int(hours) < 18:
                        send = '下午好'
                    else:
                        send = '晚上好'
                    try:
                        nickname = CustomUser.objects.get(username=user).nickname
                    except:
                        nickname = None
                    messages.add_message(request, messages.SUCCESS, '{}！{}.'.format(send, nickname))

                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '账号尚未启用')
            else:
                messages.add_message(request, messages.WARNING, '登录失败')

        else:
            messages.add_message(request, messages.INFO, '请检查字段内容')
    else:
        login_form = LoginFrom()

    template = get_template('logininfo/login.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(context=locals(), request=request)

    response = HttpResponse(html)

    return response

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, '成功注销了')
    return redirect('/')

@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            profile = CustomUser.objects.get(username=username)
        except:
            profile = CustomUser(username=username)

    if request.method == 'POST':
        profile_form = CustomUserFrom(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.INFO, '个人资料存储成功')
            return HttpResponseRedirect('/userinfo')
        else:
            messages.add_message(request, messages.INFO, '要修改资料，需要把每个字段都填写完')
    else:
        profile_form = CustomUserFrom()

    template = get_template('logininfo/userinfo.html')
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(context=locals(), request=request)

    return HttpResponse(html)

