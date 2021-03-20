# Generated by Django 2.2 on 2019-05-29 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('espaces_partage', '0010_remove_photo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]