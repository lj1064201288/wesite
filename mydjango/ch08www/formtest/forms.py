from django import forms

from .models import Post
from captcha.fields import CaptchaField


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
    class Meta:
        model = Post
        fields = [ 'mood', 'nickname', 'message', 'enabled', 'del_pass',]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '选择心情'
        self.fields['nickname'].label = '您的昵称'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '设置密码'
        self.fields['enabled'].label = '是否呈现'
        self.fields['captcha'].label = '检测你是否是机器人'