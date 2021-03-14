from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('projects/', AllProjects.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='view_project'),
]