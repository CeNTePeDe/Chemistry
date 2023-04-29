from captcha.fields import CaptchaField
from django import forms

from elements.models import Elements, Characteristics, Period, Configuration


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class ElementsForm(forms.Form):
     class Meta:
        model = Elements
        fields = '__all__'
