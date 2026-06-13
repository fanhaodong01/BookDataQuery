from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'author', 'publish_date', 'publisher')
    search_fields = ('isbn', 'title', 'author')
    list_filter = ('publish_date', 'publisher')
