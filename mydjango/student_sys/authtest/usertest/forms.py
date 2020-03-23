from django import forms

from .models import *


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'sex', 'height', 'weigh']

    def __init__(self, *args, **kwargs):
        super(UserForms, self).__init__(*args, **kwargs)

        self.fields['name'].label = '用户名'
        self.fields['password'].label = '密码'
        self.fields['sex'].label = '性别'
        self.fields['height'].label = '身高(cm)'
        self.fields['weigh'].label = '体重(kg)'

class Login_form(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    username.label = '账号'
    password.label = '密码'

class DiaryDate(forms.DateInput):
    input_type = 'date'


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {
            'ddate': DiaryDate()
        }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花费'
        self.fields['weight'].label = '今日体重'
        self.fields['note'].label = '今日心情'
        self.fields['ddate'].label = '发布时间'