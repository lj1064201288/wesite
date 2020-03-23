from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import *

class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label='标题')
    # dese = forms.CharField(widget=forms.Textarea, label="摘要", required=False)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),
    #                                   label="分类")
    # tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label="标签")
    #
    # content = forms.CharField(widget=CKEditorWidget(), label='正文', required=True)

    class Meta:
        model = Post
        fields = "__all__"