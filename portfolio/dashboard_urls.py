from django.urls import path
from . import dashboard_views

urlpatterns = [
    path('login/', dashboard_views.dashboard_login, name='dashboard_login'),
    path('logout/', dashboard_views.dashboard_logout, name='dashboard_logout'),
    path('', dashboard_views.dashboard_index, name='dashboard_index'),
    path('projects/', dashboard_views.project_list, name='dashboard_project_list'),
    path('projects/new/', dashboard_views.project_create, name='dashboard_project_create'),
    path('projects/<int:pk>/edit/', dashboard_views.project_edit, name='dashboard_project_edit'),
    path('projects/<int:pk>/delete/', dashboard_views.project_delete, name='dashboard_project_delete'),
    path('blog/', dashboard_views.blog_list, name='dashboard_blog_list'),
    path('blog/new/', dashboard_views.blog_create, name='dashboard_blog_create'),
    path('blog/<int:pk>/edit/', dashboard_views.blog_edit, name='dashboard_blog_edit'),
    path('blog/<int:pk>/delete/', dashboard_views.blog_delete, name='dashboard_blog_delete'),
]
