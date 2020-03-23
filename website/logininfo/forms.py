from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField
from mdeditor.fields import MDTextFormField, MDEditorWidget



from .models import CustomUser

User = get_user_model()

from .models import *
from captcha.fields import CaptchaField

class CustomRegsterForm(RegistrationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            User.USERNAME_FIELD,
            'nickname',
            'email',
            'sex',
            'website',
            # 'height',
            'password1',
            'password2',

        ]
        model = CustomUser
        required_css_class = 'required'


class ContactForm(forms.Form):
    CITY = [
        ['CD', '成都'],
        ['BJ', '北京'],
        ['SH', '上海'],
        ['GD', '广东'],
        ['NJ', '南京'],
    ]

    user_name = forms.CharField(max_length=50, label='您的名字', initial='李大仁')
    user_city = forms.ChoiceField(label='您的城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在校', required=False)
    user_email = forms.EmailField(label='您的邮箱')
    user_message = forms.CharField(label='您的意见', widget=forms.Textarea)

    captcha = CaptchaField(label='请输入验证码')



class PostForm(forms.ModelForm):

    captcha = CaptchaField()
    message = MDTextFormField(config_name='mood')

    class Meta:
        model = Post
        fields = '__all__'


        widgets = {
            'mood': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width:200px',
            }),
            'nickname': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:200px',
                'placeholder': '输入昵称',
                'value': '',
            }),
            'message': MDEditorWidget(attrs={
                'margin': 0
            }),
            'del_pass': forms.PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width:400px',
                'placeholder': '输入删除密码, 不设置则默认为123456',
                'value': '',
            })

        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '选择心情'
        self.fields['nickname'].label = '您的昵称'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '设置密码'
        self.fields['enabled'].label = '是否呈现'
        self.fields['captcha'].label = '验证码'
        self.initial['mood'] = 1



class LoginFrom(forms.Form):
    username = forms.CharField(max_length=30, label='用户名')
    password = forms.CharField(label='用户密码', widget=forms.PasswordInput())


class DateInput(forms.DateInput):
    input_type = 'date'

class DiaryForm(forms.ModelForm):

    note = MDTextFormField(config_name='mood')

    class Meta:
        model = Diary
        fields = ['budget', 'weight', 'note']


    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花费(元)'
        self.fields['weight'].label = '今日体重(kg)'
        self.fields['note'].label = '描述'

class CustomUserFrom(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nickname', 'email', 'height', 'website', 'sex']

    def __init__(self, *args, **kwargs):
        super(CustomUserFrom, self).__init__(*args, **kwargs)
        self.fields['height'].label = '身高(cm)'

        self.fields['website'].label = '个人网站'
        self.fields['height'].default = self.fields['height']