from rest_framework import serializers
from .models import Task
from django.utils import timezone
from datetime import timedelta

status_list = ['draft', 'in progress', 'done', 'cancelled']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_publish_date(self, value):
        if timezone.now().date() > value or value > timezone.now().date() + timedelta(days=5):
            raise serializers.ValidationError('Invalid Publish date.')
        return value

    def validate_description(self, value):
        if len(value.split()) < 10:
            raise serializers.ValidationError('minimum word count 10')
        return value

    def validate_status(self, value):
        if value not in status_list:
            raise serializers.ValidationError("status must be: 'draft', 'in progress', 'done', 'cancelled'.")
        return value