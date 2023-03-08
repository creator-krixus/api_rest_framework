from rest_framework.serializers import ModelSerializer
from ..models import Book


class Bookserializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'autor', 'editorial', 'year']
