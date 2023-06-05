from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import StackedInline

from .models import (
    SubjectModel,
    CourseModel,
    ModuleModel
)


@admin.register(SubjectModel)
class SubjectAdmin(ModelAdmin):
    list_display = [
        'title',
        'slug'
    ]
    prepopulated_fields = {
        'slug': (
            'title',
        )
    }


class ModuleInline(StackedInline):
    model = ModuleModel
    min_num = 1
    max_num = 1


@admin.register(CourseModel)
class CourseAdmin(ModelAdmin):
    list_display = [
        'title',
        'user',
        'subject',
        'description',
        'slug',
        'created_on',
        'updated_on'
    ]
    prepopulated_fields = {
        'slug': (
            'title',
        )
    }
    inlines = [
        ModuleInline
    ]
