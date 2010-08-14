from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_benchs/', include('django_benchs.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	(r'^b1/$', 'views.b1'),
	(r'^b1_1/$', 'views.b1_1'),
	(r'^b1_tpl/$', 'views.b1_tpl'),
	(r'^b2/$', 'views.b2'),
	(r'^b2_tpl/$', 'views.b2_tpl'),
	(r'^b2_1_tpl/$', 'views.b2_1_tpl'),
	(r'^header/$', 'views.header'),
)
