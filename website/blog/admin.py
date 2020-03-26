from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.html import format_html



from .models import *
from .adminforms import PostAdminForm
from website.custom_site import custom_site
from website.base_admin import BaseOwnerAdmin
# Register your models here.


# 给分类页面直接编辑文章
class PostInline(admin.StackedInline):  # StackedInline 样式不同
    '''
    可选择继承自admin.StackedInline, 以获取不同的展示样式
    '''
    fields = ('title', 'desc')

    extra = 1  # 控制额外多几个

    model = Post


# 分类模块管理后台
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'is_nav', 'created_time', 'post_count']
    fields = ('name', 'status', 'is_nav',)

    # 添加可以在分类里面进行添加文章
    inlines = [PostInline, ]

    # 设定为当前的登录用户
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)

    # 自定义展示的文章数量
    def post_count(self, obj):
        return obj.post_set.count()
    # 设置展示栏的名称
    post_count.short_description = '文章数量'


# 标签模块管理后台
@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'created_time']
    fields = ('category', 'name', 'status')

    # 设定为当前的登录用户
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


# 分类模块后台管理过滤器
class CategoryOwnerFilter(admin.SimpleListFilter):
    '''
    自定义过滤只展示当前用户分类
    '''
    title = '分类过滤器'


    parameter_name = 'owner_category'

    # 返回要展示的内容和查询用的id
    def lookups(self, request, model_admin):
        # print(request.user)
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    # 根据查询到的内容返回列表页数据
    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())

        return queryset


from mdeditor.widgets import MDEditorWidget

# 文章模块后台管理页面
@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    list_display = ['title', 'category', 'status', 'created_time', 'operator',]
    list_display_links = []

    # 添加一个过滤器
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category_name']

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

    # 引入管理表单
    form = PostAdminForm
   # actions_on_top = True
    actions_on_bottom = True
    exclude = ('owner',)

    # 编辑页面
    save_on_top = True
    #
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ( '基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category', 'tag',),
                ('status'),
            ),
        }),
        ('内容', {
            'fields':(
                'desc',
                # 'content_md',
                # 'content_ck',
                'content',
            ),
        }),

    )

    # 添加一个自定义选择栏
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>',
                           reverse('cus_admin:blog_post_change', args=(obj.id,)))
    # 设置自定义选择栏的名称
    operator.short_description = "操作"

    # 设定为当前的用户
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #
    #     return super(PostAdmin, self).save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)


    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css', ),
        }
        js= {
            'https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',
        }


