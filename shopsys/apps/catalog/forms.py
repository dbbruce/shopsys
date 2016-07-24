# coding:utf-8

from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0.')
        return self.cleaned_data['price']


class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        label='数量', widget=forms.TextInput(attrs={
            'size':'2', 'value':'1', 'class':'quantity', 'maxlength':'5'}),
        error_messages={'invalid':'请输入有效数量'},
        min_value=1)
    product_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worded():
                raise forms.ValidationError("需要启动cookie")
        return self.cleaned_data


