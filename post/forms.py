from django.forms import ModelForm
from post.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })