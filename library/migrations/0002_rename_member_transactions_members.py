# Generated by Django 3.2.12 on 2023-09-15 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='member',
            new_name='members',
        ),
    ]
