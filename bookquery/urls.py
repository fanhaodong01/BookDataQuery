from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', views.BookSearchAPIView.as_view(), name='book_search'),
    path('api/books/<str:isbn>/', views.BookDetailAPIView.as_view(), name='book_detail'),
]
