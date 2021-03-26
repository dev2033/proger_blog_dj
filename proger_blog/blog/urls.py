from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('projects/', GetProjectsListView.as_view(),
         name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(),
         name='view_project'),
    path('posts/', GetPostsListView.as_view(),
         name='posts'),
    path('post/<str:slug>/', PostDetailView.as_view(),
         name='post'),
    path('books/', BooksListView.as_view(), name='books'),
    path('book/<str:slug>', BookDetailView.as_view(), name='book'),
]