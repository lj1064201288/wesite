from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect


from .models import Post
# Create your views here.


#
# def homepage(request):
#     posts = Post.objects.all()
#     post_list = list()
#     for count, post in enumerate(posts):
#         post_list.append('No.{}: {} '.format(str(count+1), str(post)) + ' <hr>')
#         post_list.append('<small>' + str(post.body) + '</small> <br><br>')
#
#     return HttpResponse(post_list)

def homepage(request):
    template = get_template('base.html')
    posts = Post.objects.all()
    now = datetime.now()
    content = template.render(locals())

    return HttpResponse(content)


def showpost(request, slug):
    temprate = get_template('post.html')

    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            content = temprate.render(locals())

            return HttpResponse(content)

    except Exception:
        redirect('/')