from django.test import TestCase, Client
from django.urls import reverse

from .models import Book


class BookModelTests(TestCase):
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
        response = self.client.get(reverse('index'), {'search_type': 'title', 'keyword': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_search_by_author_case_insensitive(self):
        response = self.client.get(reverse('index'), {'search_type': 'author', 'keyword': 'AUTHOR'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_search_by_isbn(self):
        response = self.client.get(reverse('index'), {'search_type': 'isbn', 'keyword': '9780000000001'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_date_range_filter(self):
        response = self.client.get(reverse('index'), {
            'search_type': 'title',
            'keyword': '',
            'start_date': '2018-01-01',
            'end_date': '2019-12-31',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_date_range_open_end(self):
        response = self.client.get(reverse('index'), {
            'search_type': 'title',
            'keyword': '',
            'start_date': '2018-01-01',
            'end_date': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_detail_page(self):
        response = self.client.get(reverse('book_detail', kwargs={'isbn': '9780000000001'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        self.assertContains(response, 'A test book.')
