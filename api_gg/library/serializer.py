from rest_framework import serializers
from .models import Book, Author


class AuthorSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1