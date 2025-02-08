from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Article
from .serializer import ArticleSerializer


class ArticleListApiView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.public:
            return Response({'message': 'Can not delete published Article.'},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({'message': 'object deleted'})