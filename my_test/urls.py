from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    #(r'^fluorescence_fit/', include('fluorescence_fit.urls')),

    (r'^', include('article.urls')),
    #(r'^dpc/', include('dpc.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/login/$', 'my_test.views.login'),
    url(r'^accounts/auth/$', 'my_test.views.auth_view'),
    url(r'^accounts/logout/$', 'my_test.views.logout'),
    url(r'^accounts/loggedin/$', 'my_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'my_test.views.invalid_login'),
    url(r'^accounts/register/$', 'my_test.views.register_user'),
    url(r'^accounts/register_success/$', 'my_test.views.register_success'),

    # basic html to include all beamlines, this should be shared by each individual tool
    url(r'^accounts/all_beamlines/$', 'my_test.views.all_beamlines'),
)
