from django.urls import path

from .views import (
    MyUserLoginView
)

app_name = 'userapp'

urlpatterns = [
    path('', MyUserLoginView.as_view(), name='user_login_view')
]
