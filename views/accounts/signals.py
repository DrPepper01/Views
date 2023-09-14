from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.apps import apps


def create_author(sender, **kwargs):
    if kwargs['created']:
        instance = kwargs['instance']
        author_model = apps.get_model('views_app', 'Author')
        author_model.objects.create(name=instance.username, bio='bio', email=instance.email, user=instance)
        print(f'Был создан новый автор по имени {instance.username}')


post_save.connect(create_author, sender=User)
