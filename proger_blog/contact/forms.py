from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    first_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваше имя..."
        })
    )
    last_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваша фамилия..."
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            "placeholder": "Ваш Email..."
        })
    )
    message = forms.TextInput(
        attrs={"placeholder": "Текст сообщения..."}
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
