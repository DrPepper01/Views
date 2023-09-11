from django.test import TestCase
from .models import Author, Category
from django.contrib.auth.models import User

from django.urls import reverse
# Create your tests here.


class AuthorViewTestCase(TestCase):

    def setUp(self) -> None:
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_author_list_view_user_logged_in(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('author_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views_app/author_list.html')

    def test_author_list_view_anonymous_user(self):
        response = self.client.get(reverse('author_list'))

        self.assertEqual(response.status_code, 302)

# class TestAuthor(TestCase):
#
#     def setUp(self) -> None:
#         self.author = Author.objects.create(name='test_author',
#                                             email='test@test.com',
#                                             bio='test')
#
#     def test_get_authors(self):
#         url = reverse('author_list')
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(self.author, response.context['authors'])
#
#     def test_get_author(self):
#         url = reverse('author_detail', kwargs={'pk': self.author.pk})
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(self.author, response.context['author'])
#
#     def test_create_author(self):
#         url = reverse('author_create')
#         data = {'name': 'test_name', 'bio': 'test_bio', 'email': 'test2@test.com'}
#
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(len(Author.objects.all()), 2)
#
#
# class TestCategory(TestCase):
#
#     def setUp(self) -> None:
#         self.category = Category.objects.create(name='test_category', description='testTestTest')
#
#     def test_get_categories(self):
#         url = reverse('category_list')
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(self.category, response.context['categories'])
#
#     def test_get_author(self):
#         url = reverse('category_detail', kwargs={'pk': self.category.pk})
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(self.category, response.context['category'])
#
#     def test_create_author(self):
#         url = reverse('category_create', kwargs={'pk': self.category.pk})
#         data = {'name': 'test_name2', 'description': 'testTestTest'}
#
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(len(Category.objects.all()), 2)
#
#     def test_update_category(self):
#         url = reverse('category_update', kwargs={'pk': self.category.pk})
#         data = {'name': 'test_nameNew', 'description': 'testTestTestNew'}  #
#
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Category.objects.get(pk=self.category.pk).name, 'test_nameNew')
