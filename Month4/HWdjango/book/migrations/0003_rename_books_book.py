# Generated by Django 4.0.4 on 2022-05-17 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_books_delete_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
