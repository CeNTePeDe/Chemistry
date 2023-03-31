from captcha.fields import CaptchaField
from django import forms

from elements.models import Elements, Characteristics, Period, Configuration


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class ElementsForm(forms.Form):
    name = forms.CharField(label='Название элемента', widget=forms.widgets.Textarea())
    simbol = forms.CharField(label='Ввести символ', widget=forms.widgets.Textarea())
    image = forms.ImageField(label='', widget=forms.widgets)
    content = forms.CharField(label='об элементе', widget=forms.widgets.Textarea())
    molar_mass = forms.FloatField(label='молярная масса', widget=forms.widgets.Textarea())
    characteristics = forms.ModelChoiceField(queryset=Characteristics.objects.all(),
                                             label='характеристика', widget=forms.widgets.Select(attrs={'size': 8}))
    period = forms.ModelChoiceField(queryset=Period.objects.all(),
                                    label='период', widget=forms.widgets.Select(attrs={'size': 8}))
    configuration = forms.ModelChoiceField(queryset=Configuration.objects.all(),
                                           label='конфигурация', widget=forms.widgets.Select(attrs={'size': 8}))

    class Meta:
        model = Elements
        fields = '__all__'
