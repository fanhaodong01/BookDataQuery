from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookAPITests(TestCase):
    def setUp(self):
        Book.objects.create(
            isbn='9780000000001',
            title='Test Book',
            author='Test Author',
            publish_date='2018-06-01',
            publisher='Test Publisher',
            introduction='A test book.',
            catalog='Chapter 1',
        )

    def test_search_by_title_case_insensitive(self):
        response = self.client.get(
            reverse('book_search'),
            {'search_type': 'title', 'keyword': 'test'},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['title'], 'Test Book')

    def test_search_by_author_case_insensitive(self):
        response = self.client.get(
            reverse('book_search'),
            {'search_type': 'author', 'keyword': 'AUTHOR'},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['title'], 'Test Book')

    def test_search_by_isbn(self):
        response = self.client.get(
            reverse('book_search'),
            {'search_type': 'isbn', 'keyword': '9780000000001'},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['isbn'], '9780000000001')

    def test_date_range_filter(self):
        response = self.client.get(
            reverse('book_search'),
            {
                'search_type': 'title',
                'keyword': '',
                'start_date': '2018-01-01',
                'end_date': '2019-12-31',
            },
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['title'], 'Test Book')

    def test_date_range_open_end(self):
        response = self.client.get(
            reverse('book_search'),
            {
                'search_type': 'title',
                'keyword': '',
                'start_date': '2018-01-01',
                'end_date': '',
            },
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['title'], 'Test Book')

    def test_detail_api(self):
        response = self.client.get(
            reverse('book_detail', kwargs={'isbn': '9780000000001'}),
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['title'], 'Test Book')
        self.assertEqual(data['introduction'], 'A test book.')

    def test_detail_api_not_found(self):
        response = self.client.get(
            reverse('book_detail', kwargs={'isbn': '0000000000000'}),
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], '未找到该书籍。')
