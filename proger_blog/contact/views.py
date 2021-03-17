from django.shortcuts import render
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
from .tasks import send_beat_email


class ContactView(CreateView):
    """Отображение формы подписки по email"""
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact/contacts.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_beat_email.delay(form.instance.email)
        return super().form_valid(form)
