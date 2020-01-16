# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 16:45
# @Author  : 奔奔
# @File    : urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectsView.as_view())
]
