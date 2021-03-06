"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'psqgswdx_+p=@^2*w1+tkfpo%3kx7csnjo-9=o$lk^!v11bn-j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# 是否支持缩略图部分
THUMBNAIL_HIGH_RESOLUTION = True

# 处理缩略图的部分
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# 处理上传的文件
FILER_STORAGES = {
    'public':{
        'main':{
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS':{
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/website/media/filer',
                'base_url': '/media/filer',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/website/media/filer_thumbnails',
                'base_url': '/media/filer_thumbnails',
            },
        },
    },

    'private': {
        'main': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/website/media/smedia/filer',
                'base_url': '/smedia/filer',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/website/media/smedia/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails',
            },
        },
    },

}

# media存储位置
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/tlxy/tulingxueyuan/Django_notebook/website/media'

SITE_ID = 1

# session浏览保留数据
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #xadmin
    # 'xadmin',
    # 'crispy_forms',
    # 博客app
    'blog',
    'config',
    'comment',
    'pollitem',
    # 引入autocomplete插件
    'dal',
    'dal_select2',
    # 登录app
    'logininfo',
    # markdown
    'mdeditor',
    # 富文本
    'ckeditor',
    # 验证码
    'captcha',
    # 商城
    'cart',
    # 图片包
    'easy_thumbnails',
    'filer',
    'mptt',
    # 投票app
    'mainsite',
    # 'allauth',
    # 网站地图
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',



)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

MIDDLEWARE = [
    # 增加访问统计的时候使用
    'blog.middleware.user_id.UserIDMiddlewares',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'




# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website_liujin',
        'HOST':'localhost',
        'POST':'3306',
        'USER': 'root',
        'PASSWORD':'123456',
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
#设置图片等静态文件的路径

STATICFILES_DIRS = (
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
    ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ),
    ('upload',os.path.join(STATIC_ROOT,'upload').replace('\\','/') ),
    os.path.join(BASE_DIR, './static'),
)

# 邮箱设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'lj1064201288@163.com'
EMAIL_HOST_USER = 'lj1064201288@163.com'
EMAIL_HOST_PASSWORD = 'lj1064201288'
EMAIL_USE_TLS = True

# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # 强制注册邮箱验证(注册成功后，会发送一封验证邮件，用户必须验证邮箱后，才能登陆)
ACCOUNT_EMAIL_REQUIRED = True           # 设置用户注册的时候必须填写邮箱地址
ACCOUNT_LOGOUT_ON_GET = False           # 用户登出(需要确认)


# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
LOGIN_REDIRECT_URL = 'accounts/profile'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
AUTHENTICATION_BACKENDS = (
    # django admin所使用的用户登录与django-allauth无关
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True

CKEDITOR_UPLOAD_PATH = "article_images"


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
			['div','Source','-','Save','NewPage','Preview','-','Templates'],
			['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'],
			['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
			['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'],
			['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
			['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
			['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
			['Link','Unlink','Anchor'],
			['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
			['Styles','Format','Font','FontSize'],
			['TextColor','BGColor'],
			['Maximize','ShowBlocks','-','About', 'pbckcode'],
		),
	}
}

MDEDITOR_CONFIGS = {
    'default':{
        'width': 1200,  # 自定义编辑框宽度
        'heigth': 600,   # 自定义编辑框高度
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
        'image_floder': 'editor/blog',  # 图片保存文件夹名称
        'imageUploadURL' :'editor/blog',
        'theme': 'default',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'sequence': True  # 是否开启序列图功能
    },
    'mood':{
        'watch': False,
        'width': 400,
        'height': 200,
        'margin': 0,
        'toolbar': ['image', 'emoji'],
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        'image_floder': 'editor/mood',
        'emoji': True,  # 是否开启表情功能
        'tex': False,  # 是否开启 tex 图表功能
        'preview_theme': None,  # 预览区域主题， dark / default
        'flow_chart': False,  # 是否开启流程图功能
        'sequence': False, # 是否开启序列图功能
        'toolbar_autofixed': False,  # 工具栏是否吸顶


    }
}

# APPEND_SLASH = False