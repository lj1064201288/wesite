"""
Django settings for socialitem project.

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
SECRET_KEY = '@!35xote9-$pqn8^eq-p(t_9q0+k!$&ooekiqfv37q7uemyw6!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/mydjango/mshop/media/filer',
                'base_url': '/media/filer',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/mydjango/mshop/media/filer_thumbnails',
                'base_url': '/media/filer_thumbnails',
            },
        },
    },

    'private': {
        'main': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/mydjango/mshop/media/smedia/filer',
                'base_url': '/smedia/filer',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/home/tlxy/tulingxueyuan/Django_notebook/mydjango/mshop/media/smedia/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails',
            },
        },
    },

}

# media存储位置
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/tlxy/tulingxueyuan/Django_notebook/mydjango/mshop/media'

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
    'pollitem',
    'cart',
    'easy_thumbnails',
    'filer',
    'mptt',
    'allauth',
    'django.contrib.sites',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',

)

SITE_ID = 1

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

ROOT_URLCONF = 'socialitem.urls'

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

WSGI_APPLICATION = 'socialitem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mshop',
        'HOST':'localhost',
        'POST':'3306',
        'USER': 'root',
        'PASSWORD':'123456',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
# 设置图片等静态文件的路径
STATICFILES_DIRS = (
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
    ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ),
    ('upload',os.path.join(STATIC_ROOT,'upload').replace('\\','/') ),
)

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