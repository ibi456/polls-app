from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import Question

class QuestionTest(TestCase):
    def setUp(self):
        Question.objects.create(question_text="Yo what it is?", pub_date=timezone.now())
        Question.objects.create(question_text="Is it you boy?", pub_date=timezone.now())

    def test_question_has_text(self):
        q = Question.objects.get(id=1)
        self.assertEquals(q.question_text, "Yo what it is?")

    def test_qty_created(self):
        qs = Question.objects.all()
        self.assertEquals(qs.count(), 2)

