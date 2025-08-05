from django.urls import path
from .views import author_list, Book_list, BookDetailView
urlpatterns = [
    path('authors/', author_list , name = 'authors'),
    path('books/', Book_list.as_view() , name = 'books'),
    path('books/<int:book_pk>', BookDetailView.as_view(), name='book_detail')
    
]

