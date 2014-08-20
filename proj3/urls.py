from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'proj3_app.views.home', name='home'),
    url(r'^crimeinfo/$', 'proj3_app.views.crimeinfo', name='crimeinfo'),
    url(r'^test/$', 'proj3_app.views.test', name='test'),
    url(r'^test2/$', 'proj3_app.views.test2', name='test2'),
    url(r'^assault_count/$', 'proj3_app.views.assault_count', name='assault_count'),
    url(r'^crime_date/$', 'proj3_app.views.crime_date', name='crime_date'),
    url(r'^test3/$', 'proj3_app.views.test3', name='test3'),
    # url(r'^assault_regression/$', 'proj3_app.views.assault_regression', name='assault_regression'),
    url(r'^cat_regression/(?P<cat>\w+)/$', 'proj3_app.views.cat_regression', name='cat_regression'),
)
