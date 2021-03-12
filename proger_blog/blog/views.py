from django.shortcuts import render
from django.views.generic import ListView

from .models import Project


class Home(ListView):
    """
    Вывод главной страницы
    """
    model = Project
    context_object_name = 'projects'
    template_name = 'blog/index.html'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

