from django.views.generic import ListView

from .models import Project, Category


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
        context['title'] = 'Proger Blog : Главная'
        projects = context['projects']
        # показывает 3 последних проекта
        context['last_projects'] = projects.order_by('-id')[:3]
        context['categories'] = Category.objects.all()
        return context

