from django.conf.urls import patterns, url
from post.views import PostListView, PostDetailView, PostCreateView

urlpatterns = patterns(
    'post.views',

    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^add$', PostCreateView.as_view(), name='post-add'),

)