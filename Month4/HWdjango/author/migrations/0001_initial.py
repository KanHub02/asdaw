# Generated by Django 4.0.4 on 2022-05-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_birth', models.IntegerField()),
                ('story', models.CharField(max_length=350)),
            ],
        ),
    ]
