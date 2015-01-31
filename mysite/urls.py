from django.conf.urls.defaults import *
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from mysite.books import views
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^hello/$', hello),
    (r'^display_meta/$', display_meta),
    (r'^time/$', current_datetime),
    (r'^another-time-page/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),

    (r'^search_form/$', views.search_form),
    (r'^search/$', views.search),
)