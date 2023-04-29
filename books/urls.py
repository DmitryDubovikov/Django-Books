from django.urls import include, path
from rest_framework import routers
from books.views import BookViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
