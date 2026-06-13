from django.db import models


class Book(models.Model):
    isbn = models.CharField('ISBN', max_length=20, primary_key=True)
    title = models.CharField('书名', max_length=200)
    author = models.CharField('作者', max_length=200)
    publish_date = models.DateField('出版时间')
    publisher = models.CharField('出版社', max_length=200)
    introduction = models.TextField('简介', blank=True)
    catalog = models.TextField('目录', blank=True)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
        ordering = ['-publish_date']

    def __str__(self):
        return f'{self.title} ({self.isbn})'
