from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('taskList/<int:project_id>', views.task_List, name='task_List'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]