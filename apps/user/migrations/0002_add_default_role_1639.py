from django.db import migrations
from django.contrib.auth.models import Group


def add_default_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    admin_group, created = Group.objects.get_or_create(name='Admin')
    print("Admin group created.")
    owner_group, created = Group.objects.get_or_create(name='Owner')
    print("Owner group created.")
    user_group, created = Group.objects.get_or_create(name='User')
    print("User group created.")


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_group),
    ]
