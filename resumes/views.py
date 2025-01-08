from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Resume
from .serializers import ResumeSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for the Resume model.
    """
    queryset = Resume.objects.filter(delete_time__isnull=True)  # Only fetch non-deleted records
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def perform_create(self, serializer):
        # Set the creator as the current user
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Automatically set modification time
        serializer.save(modify_time=timezone.now())

    def perform_destroy(self, instance):
        # Soft delete: set the delete_time instead of actually deleting the record
        instance.delete_time = timezone.now()
        instance.save()
