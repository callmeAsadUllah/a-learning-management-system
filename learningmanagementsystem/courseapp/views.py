from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    FormView
)
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.permissions import (
    IsAdminUser
)
from .models import (
    CourseModel
)
from .serializers import (
    CourseSerializer
)


class CourseListView(ListView):
    context_object_name = 'courses'
    model = CourseModel
    paginate_by = 2
    queryset = CourseModel.objects.all()
    template_name = 'courseapp/list.html'
    # def get_context_data(self, **kwargs):
    #     courses = CourseModel.objects.all()
    #     context = super().get_context_data(**kwargs)
    #     context['courses'] = CourseDetailView(self.request.GET, queryset=courses)
    #     return context

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class CourseListAPIView(ListAPIView):
    model = CourseModel
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [
        IsAdminUser
    ]


class CourseDetailView(DetailView):
    context_object_name = 'course'
    model = CourseModel
    template_name = 'courseapp/detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(CourseDetailView, self).get_context_data(**kwargs)
    #     context['course'] = CourseModel.objects.get(id)
    #     return context

