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

    url(r'^category_count/(?P<cat>\w+)/$', 'proj3_app.views.category_count', name='category_count'),
    url(r'^crime_date/$', 'proj3_app.views.crime_date', name='crime_date'),
    url(r'^test3/$', 'proj3_app.views.test3', name='test3'),

    url(r'^cat_regression/(?P<cat>\w+)/$', 'proj3_app.views.cat_regression', name='cat_regression'),
)
