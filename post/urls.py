from django.conf.urls import patterns, url
from post.views import PostListView

urlpatterns = patterns('post.views',
    # Example:
    # (r'^django_dynamic_models/', include('django_dynamic_models.foo.urls')),

    url(r'^$', PostListView.as_view(), name='index'),
    url(r'cache/*$', PostListView.as_view(), name='index'),

)