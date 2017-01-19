from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^result', views.result, name='result'),
    url(r'^score', views.score, name='score'),
]
'''urls for the index and result page'''
