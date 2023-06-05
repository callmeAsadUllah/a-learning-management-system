from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

from .forms import (
    MyUserLoginForm
)


class MyUserLoginView(LoginView):
    authentication_form = MyUserLoginForm
    http_method_names = [
        'post'
    ]
    template_name = 'userapp/login.html'


class MyUserLogoutView(LogoutView):
    pass