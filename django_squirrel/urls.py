from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'goals.views.dashboard', name='dashboard'),

    url(r'^goals/', include('goals.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
