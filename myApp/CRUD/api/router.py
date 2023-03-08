from rest_framework.routers import DefaultRouter
from .views import BookApiViewset

router_books = DefaultRouter()
router_books.register(prefix='book', basename='book', viewset=BookApiViewset)
