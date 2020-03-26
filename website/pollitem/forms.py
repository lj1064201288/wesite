from django import forms
from django.forms import ModelForm
from pollitem.models import *

# 收件人表单填写
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'address', 'phone']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = '收件人姓名'
        self.fields['address'].label = '地址'
        self.fields['phone'].label = '联系号码'
