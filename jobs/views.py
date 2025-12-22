from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Job
from .serializers import JobSerializer
from django.shortcuts import get_object_or_404

class JobViewSet(viewsets.ViewSet):
    
    def list(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        job = get_object_or_404(Job, pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
