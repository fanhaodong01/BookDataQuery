from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Book 模型序列化器，用于 API 响应。"""

    class Meta:
        model = Book
        fields = [
            'isbn',
            'title',
            'author',
            'publish_date',
            'publisher',
            'introduction',
            'catalog',
        ]
