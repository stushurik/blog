from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns(
    '',

    url(r'^post/', include('post.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),

    # url(r'', include('social_auth.urls')),

) + static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
