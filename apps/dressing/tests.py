from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Annotation
from datetime import date

# Create your tests here.

# Model Tests

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(url='http://testurl.com')
    def test_article_fields(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.url, 'http://testurl.com')

class AnnotationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testname', email='test@test.com', password='testpassword')
        self.article = Article.objects.create(url='http://testurl.com')
        self.annotation = Annotation.objects.create(body='This is a test annotation.', article=self.article, user=self.user, category='question')
    def test_annotation_article_user_fields(self):
        self.assertEqual(self.annotation.body, 'This is a test annotation.')
        self.assertEqual(self.annotation.article, self.article)
        self.assertEqual(self.annotation.user, self.user)
        self.assertEqual(self.annotation.category, 'question')