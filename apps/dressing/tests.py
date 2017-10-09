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
        self.user = User.objects.create_user(username='testname', email='test@test.com', password='testpassword')
        self.article = Article.objects.create(url='http://testurl.com')
        Annotation.objects.create(body='This is a test annotation.', article=self.article, user=self.user, article_location='testlocation')
    def test_annotation_article_user_fields(self):
        annotation = Annotation.objects.get(id=1)
        self.assertEqual(annotation.body, 'This is a test annotation.')
        self.assertEqual(annotation.article, self.article)
        self.assertEqual(annotation.user, self.user)
        self.assertEqual(annotation.article_location, 'testlocation')
        self.assertContains(self.user.annotations, annotation)
        self.assertContains(self.article.annotations, annotation)