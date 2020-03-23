from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from .models import Matter, Mood

# Create your views here.


def index(request, del_pass=None, pid=None):
    matters = Matter.objects.all().order_by('-pub_time')
    moods = Mood.objects.all()
    template = get_template('index.html')

    if pid and del_pass:
        try:
            matter = Matter.objects.get(id=pid)
        except Exception as e:
            post = None
        if matter:
            if del_pass == post.del_pass:
                Matter.objects.get(id=pid).delete()
                message = '数据删除成功'
            else:
                message = '密码错误'

    html = template.render(locals())

    return HttpResponse(html)