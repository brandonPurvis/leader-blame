from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

from blame import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^blame', views.blame, name='blame'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^leaderboard', views.leaderboard, name='leaderboard'),
                       url(r'^static/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       )
