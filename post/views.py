from urllib import urlcleanup
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from blog.utils import LoginRequiredMixin
from post.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('post-list')

