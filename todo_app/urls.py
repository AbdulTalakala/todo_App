from django.urls import path
from . import views

urlpatterns = [
        path('',views.taskList,name='result'),
        path('delete/<int:id>/',views.delete,name='delete'),
        path('update/<int:id>/',views.update,name='update'),
        path('taskListview/',views.TaskListView.as_view(),name='taskListview'),
        path('details/<int:pk>/',views.TaskDetailView.as_view(),name='detail'),
        path('updateTask/<int:pk>/',views.TaskUpdateView.as_view(),name='updateTask'),
        path('deleteTask/<int:pk>/',views.TaskDeleteView.as_view(),name='deleteTask')
        # path('home',views.task,name='home')
    ]