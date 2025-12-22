from django.urls import path
from .views import JobViewSet

job_list = JobViewSet.as_view({
    'get': 'list'
})

job_detail = JobViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', job_list, name='job-list'),
    path('<int:pk>/', job_detail, name='job-detail'),
]
