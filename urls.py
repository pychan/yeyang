from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
#from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	#url(r'^media/(?P<path>.*)$','django.contrib.staticfiles.views.serve',{'document':settings.MEDIA_ROOT}),
	url(r'^index/$','cyy.views.index'),
	url(r'^get_tag/(?P<tag>.*)/$','cyy.views.get_tag'),
	url(r'^none/$','cyy.views.none'),
	url(r'^detail/(?P<num_pk>\d*)/$','cyy.views.detail'),
	url(r'^pic/$','cyy.views.pic'),
	url(r'^post_msg/$','cyy.views.post_msg'),
	url(r'^error/$','cyy.views.error'),
	url(r'^search/$','cyy.views.search'),
    # url(r'^$', 'yeyang.views.home', name='home'),
    url(r'^$', 'django.views.generic.simple.redirect_to',{'url':'/index/'}),
	url(r'^home/$','cyy.views.home'),
    # url(r'^yeyang/', include('yeyang.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
