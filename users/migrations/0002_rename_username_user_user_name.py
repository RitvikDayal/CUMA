# Generated by Django 3.2 on 2021-04-11 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user_name',
        ),
    ]
