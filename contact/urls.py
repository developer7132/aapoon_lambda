from django.conf.urls import include, url
from .views import render_form, confirm

urlpatterns = [
    url('confirm/', render_form, name='render_form'),
    url('password/', confirm, name='password'),
]

