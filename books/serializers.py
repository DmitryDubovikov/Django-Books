from rest_framework import serializers
from books.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "surname", "birth_date")


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        # fields = ("id", "title", "author", "published")
        fields = ("id", "title", "published", "description")
