from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookms.views.home', name='home'),
    # url(r'^bookms/', include('bookms.foo.urls')),
    (r'^grappelli/',include('grappelli.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bookapp.views.welcome'),
    url(r'^welcome$', 'bookapp.views.welcome'),

    url(r'^accounts/index$', 'bookapp.views.index',name="accounts_index"),
    url(r'^accounts/register$', 'bookapp.views.register',name="register"),
    url(r'^accounts/login$', 'bookapp.views.login',name="login"),
    url(r'^accounts/logout$', 'bookapp.views.logout',name="logout"),
    url(r'^accounts/edit$', 'bookapp.views.account_edit',name="edit"),
)

urlpatterns += patterns ('',
(r'^bookapp/', include('bookapp.urls')),
)

urlpatterns += staticfiles_urlpatterns()