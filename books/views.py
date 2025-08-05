from django.shortcuts import render
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def author_list(request):
    authors = Author.objects.all() # databse ma store bhako objects (models ma banako) query set bata taneko
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

class Book_list(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDetailView(APIView):
    def get(self, request, book_pk):
        try:
            books = Book.objects.get(pk=book_pk)
            serializer = BookSerializer(books)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found"}, status= 404
            )
            



