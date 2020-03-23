from django.db import models
from django.contrib.auth.models import User as AutoUser

# Create your models here.


class Mood(models.Model):
    status = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, verbose_name='选择心情')
    nickname = models.CharField(max_length=20, default='一位不愿透露姓名的勇士', verbose_name='昵称')
    message = models.TextField(null=False, verbose_name='内容/消息')
    del_pass = models.CharField(max_length=10, default=123456,)
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    enabled = models.BooleanField(default=False, verbose_name='是否呈现出来')


    def __str__(self):
        return self.message

class User(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name='用户名')
    password = models.CharField(max_length=20, null=False, verbose_name='用户密码')
    email = models.EmailField(verbose_name='邮箱')
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(AutoUser, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)

    def __str__(self):
        return self.user.username

class Diary(models.Model):
    user = models.ForeignKey(AutoUser, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateField()


    def __str__(self):
        return '{}({})'.format(self.ddate, self.user)