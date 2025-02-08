import time

from rest_framework import serializers
from .models import Article
from django.utils import timezone


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ['create_date', 'write_date']

    def create(self, validated_data):
        print(validated_data)
        validated_data['create_date'] = timezone.now()
        validated_data['write_date'] = timezone.now()
        print(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['write_date'] = timezone.now()
        return super().update(instance, validated_data)

    def validate_publish_date(self, value):
        if timezone.now().date() > value:
            raise serializers.ValidationError('Invalid Publish date.')
        return value
