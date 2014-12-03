from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields, ForeignKey, ImageField
from django.utils import encoding
from django.utils.text import slugify
import unidecode


class Post(models.Model):

    title = fields.CharField(max_length=255)
    slug = fields.SlugField(blank=True, unique=True)
    short_body = fields.CharField(max_length=255, blank=True)
    body = fields.TextField()
    author = ForeignKey(User)
    created = fields.DateTimeField(auto_now=True)
    image = ImageField(upload_to="media")

    def __str__(self):

        value = encoding.smart_unicode(self.title)

        return encoding.smart_unicode(unidecode.unidecode(value))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.short_body and self.body:

            self.short_body = self.body[:100] + "..."

        if not self.slug:

            value = encoding.smart_unicode(self.title)

            print value
            print encoding.smart_unicode(unidecode.unidecode(value))

            self.slug = slugify(unicode(encoding.smart_unicode(unidecode.unidecode(value))))

        return super(Post, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)