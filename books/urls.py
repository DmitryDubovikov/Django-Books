from django.urls import include, path
from rest_framework import routers
from books.views import BookViewSet

urlpatterns = [
    path("books/", BookViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "books/<int:pk>/",
        BookViewSet.as_view({"put": "update", "get": "retrieve", "delete": "destroy"}),
    ),
]
