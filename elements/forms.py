from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

