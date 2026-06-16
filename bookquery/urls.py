from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', views.BookSearchAPIView.as_view(), name='book_search'),
    path('api/books/<str:isbn>/', views.BookDetailAPIView.as_view(), name='book_detail'),
    path('detail/<str:isbn>/', TemplateView.as_view(template_name='books/detail.html'), name='book_detail_page'),
    path('', TemplateView.as_view(template_name='books/index.html'), name='index'),
]
