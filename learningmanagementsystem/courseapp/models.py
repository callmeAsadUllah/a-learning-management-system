from django.db import models
from django.db.models import Model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.conf import settings
from django.urls import reverse


class SubjectModel(Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'


class CourseModel(Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    subject = models.ForeignKey(
        SubjectModel,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse(
            'courseapp:CourseModel',
            args=[
                self.slug
            ]
        )

    def __str__(self):
        return f'{self.title}'


class ModuleModel(Model):
    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
        related_name='modules'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}'


class ContentModel(models.Model):
    module = models.ForeignKey(
        ModuleModel,
        on_delete=models.CASCADE,
        related_name='contents',
    )
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': (
                'text',
                'video',
                'image',
                'file'
            )
        },
        on_delete=models.CASCADE,
        related_name='contents'
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class ItemBaseModel(Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_related'
    )
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title}'


class TextModel(ItemBaseModel):
    content = models.TextField()


class FileModel(ItemBaseModel):
    file = models.FileField(upload_to='files')


class ImageModel(ItemBaseModel):
    file = models.FileField(upload_to='images')


class VideoModel(ItemBaseModel):
    url = models.URLField()
