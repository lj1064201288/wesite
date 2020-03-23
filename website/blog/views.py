from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.cache import cache
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

from website.settings import BASE_DIR

from django.contrib.auth.models import User
from comment.models import Comment
from comment.forms import CommentForm
from .models import Post, Tag, Category
from config.models import SideBar

# Create your views here.

class CommonViewMinxin:
    def get_context_data(self, **kwargs):
        context = super(CommonViewMinxin, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            username = self.request.user.username
            useremail = self.request.user.email
            context.update({
                'username': self.request.user.username,
                'useremail': self.request.user.email
            })
        context.update({
            'sidebars': SideBar.get_all(),
            'owner': User.objects.all(),

        })

        context.update(Category.get_navs())
        return context


class PostDetailView(CommonViewMinxin, DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    # model = Post
    # template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context.update({
            'comment_form': CommentForm,
            'comment_list': Comment.get_by_target(self.request.path).order_by('-id'),
        })
        return context

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        # Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)
        # self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid

        pv_key = 'pv:%s:%s' % (uid, self.request.path)
        uv_key = 'pv:%s:%s:%s' %(uid, str(date.today()), self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key, 1, 1*60)  # 1分钟有效

        if not cache.get(uv_key):
            increase_uv = True
            cache.set(pv_key, 1, 24*60*60) # 24小时有效

        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)

        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)

        # 调试用
        # from django.db import connection
        # print(connection.queries)
        # return response

class IndexView(CommonViewMinxin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 20
    context_object_name = 'post_list' # 如果不设置此项， 在模板中需要使用object_list变量
    template_name = 'blog/list.html'


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        return context


class AuthorView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data()
        return context

    def get_queryset(self):
        queryset = super(AuthorView, self).get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)


class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update(
            {
                'keyword': self.request.GET.get('keyword', '')
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        '''重写queryset, 根据分类过滤'''
        queryset = super(CategoryView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)

class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        '''重写queryset, 根据标签过滤'''
        qyeryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return qyeryset.filter(tag_id=tag_id)

from django.template.loader import get_template
from django.template import RequestContext
from .forms import PostForm

def post(request):
    template = get_template('post.html')
    postform = PostForm()
    request_content = RequestContext(request)
    request_content.push(locals())
    html = template.render(context=locals(), request=request)

    return HttpResponse(html)