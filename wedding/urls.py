from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^when/$', views.when, name='when'),
    url(r'^where/$', views.where, name='where'),
    url(r'^why/$', views.why, name='why'),
    url(r'^how/$', views.how, name='how')
]
