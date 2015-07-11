from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

from blame import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^db', views.db, name='db'),
                       url(r'^blame', views.blame, name='blame'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^main', views.main_page, name='main'),
                       url(r'^static/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       )
