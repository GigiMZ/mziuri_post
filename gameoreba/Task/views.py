from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializer import TaskSerializer


class TaskCreateListApiView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != 'cancelled':
            return Response({'message': 'Can not delete. status must be canceled.'},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({'message': 'object deleted'})