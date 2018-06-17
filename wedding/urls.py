from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^when/$', views.when, name='when'),
    url(r'^where/$', views.where, name='where'),
    url(r'^why/$', views.why, name='why'),
    url(r'^how/$', views.how, name='how'),
    url(r'^wedding-party/$', views.wedding_party, name='wedding-party'),
    url(r'^rehearsal/$', views.wedding_party, name='wedding-party'),
    url(r'^rehearsal-dinner/$', views.dinner, name='dinner'),
    url(r'^family/$', views.family, name='family'),
    url(r'^family-rehearsal/$', views.family_rehearsal, name='family-rehearsal'),
    url(r'^vote/$', views.vote, name='vote')
]
