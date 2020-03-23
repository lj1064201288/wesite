from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# from captcha.fields import CaptchaField


from .models import *
from .forms import *

# Create your views here.



def index(request, pid=None, del_pass=None):
    template = get_template('index.html')
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()

    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['user_mood']

    except Exception as e:
        user_id = None
        message = '如果要张贴信息，需要每一个字段都填写'

    if pid and del_pass:
        try:
            post = Post.objects.get(id=pid)
        except Exception as e:
            post = None
        if post:
            if del_pass == post.del_pass:
                Post.objects.get(id=pid).delete()
                message = '数据删除成功'

            else:
                message = '密码错误'

    elif user_id != None:
        mood= Mood.objects.get(status=user_mood)
        post = Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.enabled = True
        post.save()
        # message = '{}'.format(user_pass)
        pw = user_pass

    html = template.render(locals())


    return HttpResponse(html)


def listing(request):
    template = get_template('listing.html')
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = Mood.objects.all()

    html = template.render(locals())

    return HttpResponse(html)



def posting(request):
    template = get_template('posting.html')
    message = '如果需要张贴，则需要所有的字段都要填写...'
    captcha = ContactForm()
    if request.method == 'POST':
        try:
            user_id = request.POST['user_id']
            user_pass = request.POST['user_pass']
            user_post = request.POST['user_post']
            user_mood = request.POST['mood']

            message = '发布帖子成功!!!'

        except Exception as e:
            user_id = None
            message = '请正确填写相关字段!'

        if user_id != None:
            mood = Mood.objects.get(status=user_mood)
            post = Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.enabled = True
            post.save()
    posts = Post.objects.all()
    moods = Mood.objects.all()
    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(context=locals(), request=request)

    return HttpResponse(html)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = '感谢您的来信.'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
        else:
            message = '请正确填写内容'
    else:
        form = ContactForm()

    template = get_template('contact.html')
    forms = ContactForm()
    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(context=locals(), request=request)

    return HttpResponse(html)

def post2db(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            message = '发布成功，不过需要等待管理员查看后才能正常发布!'
            post_form.save()
            return HttpResponseRedirect('/list/')

        else:
            message = '如果您需要张贴，需要每个字段都要填写...'

    else:
        post_form = PostForm()
        message = '如果您要张贴，需要每个字段都要填写'

    template = get_template('post2db.html')
    request_content = RequestContext(request)
    request_content.push(locals())

    html = template.render(context=locals(), request=request)


    return HttpResponse(html)

