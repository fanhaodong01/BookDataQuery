from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BookSearchAPIView(APIView):
    """
    书籍搜索 API。

    支持通过以下查询参数进行筛选：
    - search_type: 搜索类型，可选值为 title（默认）/ author / isbn
    - keyword: 搜索关键词
    - start_date: 起始出版时间（包含）
    - end_date: 结束出版时间（包含）

    当未提供任何 keyword 或日期范围时，返回空结果列表。
    """

    def get(self, request):
        search_type = request.query_params.get('search_type', 'title')
        keyword = request.query_params.get('keyword', '').strip()
        start_date = request.query_params.get('start_date', '').strip()
        end_date = request.query_params.get('end_date', '').strip()

        filters = Q()

        if keyword:
            if search_type == 'isbn':
                filters &= Q(isbn__icontains=keyword)
            elif search_type == 'author':
                filters &= Q(author__icontains=keyword)
            else:  # title
                filters &= Q(title__icontains=keyword)

        if start_date:
            filters &= Q(publish_date__gte=start_date)
        if end_date:
            filters &= Q(publish_date__lte=end_date)

        has_search = bool(keyword or start_date or end_date)
        books = Book.objects.filter(filters) if has_search else Book.objects.none()

        serializer = BookSerializer(books, many=True)
        return Response({
            'search_type': search_type,
            'keyword': keyword,
            'start_date': start_date,
            'end_date': end_date,
            'count': books.count(),
            'results': serializer.data,
        })


class BookDetailAPIView(APIView):
    """
    书籍详情 API。

    根据 ISBN 返回单本书籍的完整信息。
    """

    def get(self, request, isbn):
        try:
            book = Book.objects.get(pk=isbn)
        except Book.DoesNotExist:
            return Response(
                {'detail': '未找到该书籍。'},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = BookSerializer(book)
        return Response(serializer.data)
