from rest_framework import serializers
from books.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "surname", "birth_date")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "published", "description", "author")
        read_only_fields = ("author",)
