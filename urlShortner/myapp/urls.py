from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns= [
    path('task',views.task_page),
    path('hello', views.hello_world),
    path('', views.home_page)
    ]

