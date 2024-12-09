from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """ 
Serializing all the Books 
"""
    search_url = serializers.SerializerMethodField('get_search_url')
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'author', 'search_url')
    
    def get_search_url(self, obj):
        return f"http://www.isbnsearch.org/isbn/{obj.isbn}"

class AuthorSerializer(serializers.ModelSerializer):
    """ 
Serializing all the Authors 
"""
    books = BookSerializer(read_only=True, many=True, source="book_set")
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')
