from django.views.generic import ListView, DetailView

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


class ProjectDetailView(DetailView):
    """Вывод каждого проекта"""
    model = Project
    context_object_name = 'project'
    template_name = 'blog/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proger Blog'
        return context


class AllProjects(ListView):
    """Вывод всех проектов"""
    model = Project
    context_object_name = 'projects'
    template_name = 'blog/projects.html'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proger Blog : Проекты'
        return context
