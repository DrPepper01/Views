from django.test import TestCase
from .models import Author, Category
from django.contrib.auth.models import User, Permission

from django.urls import reverse

from django.apps import apps


# class TestUser(TestCase):
#
#     def test_register_new_user(self):
#         data = {
#             'username': 'test_user',
#             'password1': 'test_password',
#             'password2': 'test_password',
#             'email': 'test@test.com',
#             'first_name': 'test_first_name',
#             'last_name': 'test_last_name'
#         }
#
#         response = self.client.post(reverse('user_register'), data=data)
#
#         self.assertEqual(response.status_code, 302)
#         author_model = apps.get_model('views_app', 'Author')
#         author = author_model.objects.get(name=data['username'])
#         self.assertEqual(author.email, data['email'])
#

class AuthorViewTestCase(TestCase):

    def setUp(self) -> None:
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.superuser = User.objects.create_user(username='superuser', password='superuser',
                                                  is_superuser=True)
        self.user_with_permissions = User.objects.create_user(username='user_with_permissions',
                                                              password='permissions')

        perm = Permission.objects.get(codename='delete_author')
        perm1 = Permission.objects.get(codename='delete_category')
        self.user_with_permissions.user_permissions.add(perm, perm1)

    def test_author_list_view_user_logged_in(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('author_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views_app/author_list.html')

    def test_author_list_view_anonymous_user(self):
        response = self.client.get(reverse('author_list'))

        self.assertEqual(response.status_code, 302)

    def test_create_author(self):
        self.client.force_login(self.superuser)

        response = self.client.get(reverse('author_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views_app/form.html')

    def test_create_author_anonymous_user(self):
        response = self.client.get(reverse('author_create'))

        self.assertEqual(response.status_code, 302)

    def test_create_author_post(self):
        self.client.force_login(self.superuser)
        author_name = 'test_author'
        author_email = 'test@test.com'

        response = self.client.post(reverse('author_create'),
                                    data={'name': author_name,
                                          'bio': 'test_bio',
                                          'email': author_email})

        self.assertEqual(response.status_code, 302)
        Author.objects.get(email=author_email)

    def test_delete_author_view(self):
        author_email = 'test2@test.com'
        new_author = Author.objects.create(name='test_author', bio='bio', email=author_email)
        self.client.force_login(self.user_with_permissions)

        response = self.client.post(reverse('author_delete', args=[new_author.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Author.objects.filter(pk=new_author.pk).exists())

    def test_create_category_view(self):
        self.client.force_login(self.superuser)
        category_name = 'test_name'

        response = self.client.post(reverse('category_create'), data={'name': category_name,
                                                                      'description': 'test_description'})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name=category_name).exists())

    def test_delete_category_view(self):
        category_name = 'test_name'
        new_category = Category.objects.create(name=category_name, description='test_description')
        self.client.force_login(self.user_with_permissions)

        response = self.client.post(reverse('delete_category', args=[new_category.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(name=category_name).exists())

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
