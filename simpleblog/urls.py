from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from posts.feeds import LatestEntriesFeed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleblog.views.home', name='home'),
    url(r'^list_posts/$', 'posts.views.list_posts', name="list_posts"),
    url(r'^post_detail/(?P<post_id>\d+)/$', 'posts.views.post_detail', name="post_detail"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^threadedcomments/', include('threadedcomments.urls')),
    (r'^feed/$', LatestEntriesFeed()),
)


urlpatterns += staticfiles_urlpatterns()
