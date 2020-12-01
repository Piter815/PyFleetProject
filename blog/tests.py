import datetime

from django.test import TestCase
from django.utils import timezone

from core.models import Post, EMPTY_EMPLOYEE, Employee


class PostModelTests(TestCase):

    def test_was_published_in_future(self):
        time = timezone.now()
        future_question = Post(date_posted=time)
        true = False
        if future_question.date_posted > time:
            true = True
        self.assertIs(true, False)

    def test_with_an_user(self):
        employee = Employee(name='Alicja', surname='Makocka')
        post = Post(author=employee)
        self.assertIsNot(post.author, EMPTY_EMPLOYEE)