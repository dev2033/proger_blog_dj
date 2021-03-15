from django.db.models import F
from django.views.generic import ListView, DetailView

from .models import Project, Category, Post


class Home(ListView):
    """Вывод главной страницы"""
    model = Project
    context_object_name = 'projects'
    template_name = 'blog/index.html'

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
        projects = Project.objects.all()
        # показывает 3 последних проекта
        context['last_projects'] = projects.order_by('-id')[:3]
        context['categories'] = Category.objects.all()
        return context


class GetProjectsListView(ListView):
    """Вывод всех проектов"""
    model = Project
    context_object_name = 'projects'
    template_name = 'blog/projects.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proger Blog : Проекты'
        return context


class GetPostsListView(ListView):
    """Выводит все посты для блога"""
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proger Blog : Посты'
        return context


class PostDetailView(DetailView):
    """Показывает каждый пост отдельно"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # выражение, которое увеличивает кол-во просмотров
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['title'] = 'Proger Blog'
        return context
