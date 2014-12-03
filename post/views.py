from django.views.generic import ListView
from post.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 2
