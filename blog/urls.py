from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    url(r'^post/', include('post.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
