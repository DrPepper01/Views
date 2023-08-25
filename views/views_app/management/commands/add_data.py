from django.core.management.base import BaseCommand
from views_app.models import Author, Category, Post


class Command(BaseCommand):
    help = 'Наполняет базу данных новыми данными'

    def handle(self, *args, **kwargs):

        for obj in Author.objects.all():
            obj.delete()

        for obj in Category.objects.all():
            obj.delete()

        for obj in Post.objects.all():
            obj.delete()

        # authors
        author_1 = Author.objects.create(name='Джон', email='john@mail.com')
        author_2 = Author(name='Джейн', email='jane@mail.com')
        author_2.save()
        author_3 = Author.objects.create(name='Тим', email='tim@mail.com')

        # categories
        category_1 = Category.objects.create(name='Путешествия')
        category_2 = Category.objects.create(name='Еда')
        category_3 = Category.objects.create(name='Технологии')
        category_4 = Category.objects.create(name='Искусство')

        # post
        post_1 = Post.objects.create(title='Прогулки', content='Прогулки по городу', author=author_1, status='p')
        post_1.categories.add(category_1, category_4)
        post_2 = Post.objects.create(title='Вечера в городе', content='Еда и рестораны', author=author_2)
        post_2.categories.add(category_2, category_1)
        post_3 = Post.objects.create(title='Python', content='Программирование', author=author_3, status='p')
        post_3.categories.add(category_3)
        post_4 = Post.objects.create(title='AI', content='ИИ', author=author_3, status='p')
        post_4.categories.add(category_4)

