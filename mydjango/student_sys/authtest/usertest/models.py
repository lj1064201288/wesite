from django.db import models
from django.contrib.auth.models import User as AuthUser

from datetime import datetime

# Create your models here.


class User(models.Model):

    SEX = (
        ('0', '男'),
        ('1', '女'),
    )


    name = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=30, verbose_name='密码')
    sex = models.CharField(max_length=5, choices=SEX, default=0, verbose_name='性别')
    height = models.PositiveIntegerField(default=160, verbose_name='身高(cm)')
    weigh = models.PositiveIntegerField(verbose_name='体重(kg)')
    created_date = models.TimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class ProUser(models.Model):
    MAN = '男'
    WOMAN = '女'
    SEX = (
        (MAN, '男'),
        (WOMAN, '女'),
    )

    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    sex = models.CharField(max_length=5, choices=SEX, default=MAN)
    height = models.PositiveIntegerField(default=160, verbose_name='身高(cm)')
    weigh = models.PositiveIntegerField(verbose_name='体重(kg)')
    website = models.URLField(null=True)


    def __str__(self):
        return self.user.username

class Diary(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    budget = models.FloatField(default=0, verbose_name='今日花费')
    weight = models.FloatField(default=0, verbose_name='今日体重')
    note = models.TextField()
    ddate = models.DateField()


    def __str__(self):
        return '{}:({})'.format(self.ddate, self.user.username)