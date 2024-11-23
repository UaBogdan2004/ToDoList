from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/toggle/', views.toggle_task_status, name='toggle_task_status'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task')
]
