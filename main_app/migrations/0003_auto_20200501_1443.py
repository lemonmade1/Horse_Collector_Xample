# Generated by Django 3.0.5 on 2020-05-01 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200501_0632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='cat',
            new_name='horse',
        ),
    ]
