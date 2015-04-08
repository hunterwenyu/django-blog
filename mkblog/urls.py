from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
from datetime import date

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mkblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/', views.index, {'year': 2014}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/(\d{4})/$', views.index),
    url(r'^index/', views.index, {'year': date.today().year}),
    url(r'^blog/(\d+)/$', views.get_blog),

)
