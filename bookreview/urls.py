from . import views
from django.urls import path,include

urlpatterns = [
    path('bookreview/authors/', views.AuthorView.as_view(), name='authors'),
    path('bookreview/authors/<int:pk>', views.AuthorInstanceView.as_view(), name='author-instance'),
    path('bookreview/books/', views.BookView.as_view(), name='books'),
    path('bookreview/books/<int:pk>', views.BookInstanceView.as_view(), name='book-instance'),
    # Vista tradicional para la plantilla
    path('bookreview/', views.index_view, name='index'),
]