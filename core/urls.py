from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/new/', views.post_job, name='post_job'),
    path('register/', views.register, name='register'),
]
