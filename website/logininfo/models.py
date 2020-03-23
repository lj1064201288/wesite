from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
import mistune
# Create your models here.


class Mood(models.Model):
    status = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.status


    class Meta:
        verbose_name = verbose_name_plural = "心情"


class Post(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, verbose_name='选择心情')
    nickname = models.CharField(max_length=20, default='', verbose_name='昵称')
    message = MDTextField(null=False, verbose_name='内容/消息')
    message_html = MDTextField(null=True, blank=True, verbose_name='markdown', default='')
    del_pass = models.CharField(max_length=10, default=123456, blank=True, null=True)
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    enabled = models.BooleanField(default=False, verbose_name='是否呈现出来')


    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = mistune.markdown(self.message)
        super(Post, self).save(*args, **kwargs)



class CustomUser(User):
    SEX_ITEMS = (
        (1, '男'),
        (2, '女'),
    )

    nickname = models.CharField(max_length=100, default=None, verbose_name='昵称')
    sex = models.PositiveIntegerField(choices=SEX_ITEMS, default=1, verbose_name='性别')
    website = models.URLField(null=True, blank=True, verbose_name='个人网站(非必填)')
    height = models.PositiveIntegerField(default=160, verbose_name='身高（cm）')


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.FloatField(default=0, verbose_name='今日花费')
    weight = models.FloatField(default=0, verbose_name='身高')
    note = MDTextField(null=False, verbose_name='内容/消息')
    ddate = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')


    def __str__(self):
        return '{}({})'.format(self.ddate, self.user)

    def save(self, *args, **kwargs):
        self.note = mistune.markdown(self.note)
        super(Diary, self).save(*args, **kwargs)