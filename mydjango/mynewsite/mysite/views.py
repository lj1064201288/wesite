from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.loader import get_template

import time, random
from .models import Product

# def about(request):
#     # 主页页面的Html信息
#     html = '''
#         <!DOCTYPE  html>
#         <html>
#             <head>
#                 <meta charset="utf8" />
#                 <title>主页</title>
#             </head>
#             <body>
#                 <h2 >My index</h2>
#                 <hr />
#                 <p>Hi! Welcome to my Home</p>
#             </body>
#         </html>
#     '''
#     # 返回页面
#     return HttpResponse(html)
#
# def  listing(request):
#     # 讲models的数据映射到一个对象当中
#     product = Product.objects.all()
#
#     html = '''
#         <!DOCTYPE  html>
#         <html>
#             <head>
#                 <meta charset="utf8" />
#                 <title>产品列表</title>
#             </head>
#             <body>
#                 <table width=400 border=1 bgcolor="yellow">{}</table>
#             </body>
#         </html>
#     '''
#     # 编辑表格的菜单页面
#     tags = '<tr><td>产品名称</td><td>价格</td><td>库存</td></tr>'
#
#     # 将商品依次渲染到页面当中
#     for p in product:
#         tags = tags + '<tr><td>{}</td>'.format(p.name)
#         tags = tags + '<td>{}</td>'.format(p.price)
#         tags = tags + '<td>{}</td></tr>'.format(p.qty)
#
#     # 反馈商品的列表页面
#     return HttpResponse(html.format(tags))
#
# def disp_detail(request, sku):
#
#     html = '''
#         <!DOCTYPE  html>
#         <html>
#             <head>
#                 <meta charset="utf8" />
#                 <title>{}</title>
#             </head>
#             <body>
#                 <h2>{}</h2>
#                 <table width=400 border=1 bgcolor="yellow">{}</table>
#                 <a href="/list">返回列表</a>
#             </body>
#         </html>
#     '''
#     try:
#         product = Product.objects.get(sku=sku)
#     except Product.DoesNotExist:
#         raise Http404
#
#     # finally:
#     #     time.sleep(2)
#     #     return reverse(listing)
#     tags = '<tr><td>产品编号</td><td>{}</td></tr>'.format(product.sku)
#     tags += '<tr><td>名称</td><td>{}</td></tr>'.format(product.name)
#     tags += '<tr><td>价格</td><td>{}</td></tr>'.format(product.price)
#     tags += '<tr><td>库存</td><td>{}</td></tr>'.format(product.qty)
#
#     return HttpResponse(html.format(product.name, product.name, tags))


def about(request):
    template = get_template('about.html')

    quotes = [
        "You can't kill the deep roots by cutting off a few top branches.一棵树不会因为顶端的枝桠被截断就失去生命。",
        "有时候，我们不得不坚强，于是乎，在假装坚强中，就真的越来越坚强。",
        "明天的希望，让我们忘了今天的痛苦。",
        "Tomorrow's hope, let us forget today's pain.",
    ]

    html = template.render(context={'quote': random.choice(quotes)})

    return HttpResponse(html)


def listing(request):
    template = get_template('listing.html')
    product = Product.objects.all()

    html = template.render({'product': product})

    return HttpResponse(html)



def disp_detail(request, sku):
    template = get_template('desp_detail.html')

    try:
        product = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404

    html = template.render({'product': product})

    return HttpResponse(html)

def index(request):
    template = get_template('base.html')
    html = template.render()

    return HttpResponse(html)