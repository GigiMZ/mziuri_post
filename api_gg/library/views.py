from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer


@api_view
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(instance=books, many=True)
    return Response(serializer.data)