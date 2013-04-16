from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'goals.views.dashboard', name='goals_dashboard'),
    url(r'^list/$', 'goals.views.home', name='goals_home'),
)
