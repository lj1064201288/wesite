from django import forms

from .models import *


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['name', 'enabled']


    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '话题'
        self.fields['enabled'].label = '是否应用'

class PollitemForm(forms.ModelForm):
    class Meta:
        model = PollItem
        fields = ['name', 'vote', 'images_url']

    def __init__(self, *args, **kwargs):
        super(PollitemForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '选项名称'
        self.fields['vote'].label = '默认票数'
        self.fields['images_url'].label = '图片(可以为空)'