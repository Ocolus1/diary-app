# Generated by Django 3.1.1 on 2020-09-27 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diary', to=settings.AUTH_USER_MODEL),
        ),
    ]
