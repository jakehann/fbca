from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hotcomment/$', 'hotcomment.views.response'),
    url(r'^pagelist/$','wwwfront.views.pagelist'),
    url(r'^postlist/$','wwwfront.views.postlist'),
    url(r'^postDetails/$','wwwfront.views.postDetails'),
    # Examples:
    # url(r'^$', 'fbca.views.home', name='home'),
    # url(r'^fbca/', include('fbca.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
