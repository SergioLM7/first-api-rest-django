from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorInstanceView(generics.RetrieveAPIView):
    """ 
Returns a single author. 
Also allows updating and deleting 
"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookInstanceView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def index_view(request):
    """ 
Ensure the user can only see their own profiles. 
"""
    response = {
        'authors': Author.objects.all(),
        'books': Book.objects.all(), 
    }
    return render(request, 'bookreview/index.html', response)