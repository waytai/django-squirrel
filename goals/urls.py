from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'goals.views.home', name='goals_home'),
)
