from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Book


def index(request):
    search_type = request.GET.get('search_type', 'title')
    keyword = request.GET.get('keyword', '').strip()
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()

    filters = Q()

    if keyword:
        if search_type == 'isbn':
            filters &= Q(isbn__icontains=keyword)
        elif search_type == 'author':
            filters &= Q(author__icontains=keyword)
        else:  # title
            filters &= Q(title__icontains=keyword)

    # 出版时间范围筛选
    if start_date:
        filters &= Q(publish_date__gte=start_date)
    if end_date:
        filters &= Q(publish_date__lte=end_date)

    has_search = bool(keyword or start_date or end_date)
    books = Book.objects.filter(filters) if has_search else Book.objects.none()

    context = {
        'books': books,
        'search_type': search_type,
        'keyword': keyword,
        'start_date': start_date,
        'end_date': end_date,
        'has_search': has_search,
    }
    return render(request, 'books/index.html', context)


def book_detail(request, isbn):
    book = get_object_or_404(Book, pk=isbn)
    return render(request, 'books/detail.html', {'book': book})
