# from django.conf.urls.defaults import *
from django.urls import re_path, include
from . import views

urlpatterns = [
    #'madrona.analysistools.views',
    re_path(r'^(?P<uid>[\w_]+)/progress.json$', views.progress, name='analysis-progress'),
    re_path(r'^(?P<uid>[\w_]+)/progress.html$', views.progress_html, name='analysis-html-progress'),
]
