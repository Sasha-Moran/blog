from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from tinymce import models as tinymce_models


class AdvancedUser(AbstractUser):
    image = models.ImageField(upload_to='user-pictures/',
                              default='default-user-picture/default_user_pic.jpg',
                              verbose_name='User picture',
                              null=True)


class Post(models.Model):
    author = models.ForeignKey(AdvancedUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='post_images/',
                              verbose_name='Post image',
                              null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['-published_date']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title
