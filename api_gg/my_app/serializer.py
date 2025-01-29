from rest_framework import serializers
from .models import Post
from datetime import datetime


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.write_date = datetime.now()
        instance.edited = True
        return instance


    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.title = instance.title.upper()
        instance.create_date = datetime.now()
        return instance


    def validate_create_date(self, value):
        print(value)
        print(datetime.today())
        if str(value)[:10] != str(datetime.today())[:10]:
            raise serializers.ValidationError("Invalid Date!")
        return value
