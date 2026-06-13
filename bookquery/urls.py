from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('book/<str:isbn>/', views.book_detail, name='book_detail'),
]
