from django.conf.urls import patterns, include, url


urlpatterns = patterns('article.views',
    url(r'^all_functions/$', 'all_functions'),
    #url(r'^all_beamlines/$', 'all_beamlines'),
    url(r'^status/$', 'beamline_status'),
    url(r'^publications/$', 'all_publications'),
    url(r'^data_tool/$', 'tools'),
    url(r'^contacts/$', 'contacts_infor'),
    url(r'^login/$', 'contacts_infor'),

)
