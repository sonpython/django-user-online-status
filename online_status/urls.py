import django

if django.get_version() >= '1.6.0':
    from django.conf.urls import *
else:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^test/$', 'online_status.views.test', name="online_users_test"),
    url(r'^example/$', 'online_status.views.example', name="online_users_example"),
    url(r'^$', 'online_status.views.users', name="online_users"),
)
