from django import forms

from .models import *


class PollItemForm(forms.ModelForm):
    class Meta:
        model = PollItem
        fields = ['name', 'image_url']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:300px; border: green 1px solid',
                'placeholder': '请填写您要添加的选项',
            }),
            'image_url': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:200px; border: green 1px solid',
                'placeholder': '请输入图片网址(可不填)',
            })
        }

    def __init__(self, *args, **kwargs):
        super(PollItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '添加选项'
        self.fields['image_url'].label = '图片'



class PollForm(forms.ModelForm):

    class Meta:
        model = Poll

        fields = ['name', ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:300px; border: green 1px solid',
                'placeholder': '请填写您要添加的话题',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '话题名称'
