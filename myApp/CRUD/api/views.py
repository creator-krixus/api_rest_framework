from rest_framework.viewsets import ModelViewSet
from ..models import Book
from .seriealizers import Bookserializer


class BookApiViewset(ModelViewSet):
    serializer_class = Bookserializer
    queryset = Book.objects.all()

# Se crea una api rapidadmente con rest_framework
# Aqui fue
