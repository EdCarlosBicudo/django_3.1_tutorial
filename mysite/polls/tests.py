import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """was_published_recently() retorna False para questões com
        a data de publicação no futuro.
        """
        time = timezone.now().date() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """was_published_recently() retorna False para questões publicadas
        a mais de um dia.
        """
        time = timezone.now().date() - datetime.timedelta(days=2, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """was_published_recently() retorna True para questões publicadas
        a menos de um dia.
        """
        time = timezone.now().date() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)