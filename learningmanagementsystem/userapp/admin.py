from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import (
    MyUser
)


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = [
        'email',
        'full_name',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_admin',
        'created_on',
        'updated_on'
    ]

    readonly_fields = [
        'created_on',
        'updated_on'
    ]

    list_filter = [
        'is_admin'
    ]

    fieldsets = [
        (
            'User', {
                'fields': [
                    (
                        'full_name'
                    ),
                    (
                        'email'
                    ),
                    (
                        'first_name',
                        'last_name'
                    ),
                    (
                        'password'
                    ),
                    (
                        'updated_on',
                        'created_on'
                    )
                ]
            }
        ),
        (
            'Permission', {
                'fields': [
                    'is_active',
                    'is_admin'
                ]
            }
        )
    ]

    add_fieldsets = [
        (
            'User',
            {
                'fields': [
                    (
                        (
                            'email',
                            'password'
                        )
                    )
                ]
            },
        ),
    ]

    search_fields = [
        'email'
    ]

    ordering = []

    filter_horizontal = []

    actions_on_top = False
    actions_on_bottom = True


admin.site.unregister(Group)
