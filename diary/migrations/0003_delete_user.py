# Generated by Django 3.1.1 on 2020-09-26 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
