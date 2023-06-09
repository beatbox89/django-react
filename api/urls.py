"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),

    path('api/todo-list', views.todoList, name="todo-list"),
    path('api/todo-create', views.todoCreate, name="todo-create"),
    path('api/todo-detail/<int:pk>', views.todoDetail, name="todo-detail"),
    path('api/todo-update/<int:pk>', views.todoUpdate, name="todo-update"),
    path('api/todo-delete/<int:pk>', views.todoDelete, name="todo-delete"),
]

urlpatterns = format_suffix_patterns(urlpatterns) # djangorestframework
