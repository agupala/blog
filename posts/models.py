from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created"]

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle")
    content = RichTextField(verbose_name="Content")
    published = models.DateTimeField(default=now, verbose_name="Published Date")
    image = models.ImageField(verbose_name="Image", upload_to="blog", null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Is Published")
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.DO_NOTHING, null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["created"]

    def __str__(self):
        return self.title


