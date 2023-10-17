from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('create-new/', CreateTask.as_view(), name='task-create'),
    path('edit/<int:pk>/', EditTask.as_view(), name='task-update'),
]