from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Initialize groups and permissions'

    def handle(self, *args, **kwargs):
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        perms = Permission.objects.filter(content_type__app_label='bookshelf', codename__in=[
            'can_view', 'can_create', 'can_edit', 'can_delete'
        ])

        editors.permissions.set(perms.filter(codename__in=['can_create', 'can_edit']))
        viewers.permissions.set(perms.filter(codename='can_view'))
        admins.permissions.set(perms)

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully.'))

