from django.urls import path

from .views import (
    CourseListView,
    CourseListAPIView,
    CourseDetailView,
    # CourseCreateView
)

app_name = 'courseapp'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list_view'),
    path('api/', CourseListAPIView.as_view(), name='course_list_api_view'),
    # path('add/', CourseCreateView.as_view(), name='course_create_view'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail_view'),
]

