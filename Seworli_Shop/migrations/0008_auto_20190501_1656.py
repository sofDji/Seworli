# Generated by Django 2.2 on 2019-05-01 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seworli_Shop', '0007_auto_20190501_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trepied',
            name='author',
        ),
        migrations.DeleteModel(
            name='Sac',
        ),
        migrations.DeleteModel(
            name='Trepied',
        ),
    ]