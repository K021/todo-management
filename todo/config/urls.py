"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo.views import todo_list, todo_add, todo_detail, todo_delete, todo_change, todo_complete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', todo_list, name='main'),
    path('todos/add/', todo_add, name='todo_add'),
    path('todos/complete/<slug:pk>/', todo_complete, name='todo_complete'),
    path('todos/delete/<slug:pk>/', todo_delete, name='todo_delete'),
    path('todos/change/<slug:pk>/', todo_change, name='todo_change'),
    path('todos/<slug:pk>/', todo_detail, name='todo_detail'),
    path('todos/<slug:pk>/<slug:ask_delete>/', todo_detail,  name='todo_detail_modal'),
]
