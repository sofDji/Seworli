# Generated by Django 2.2 on 2019-05-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20190509_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='yanotif',
            field=models.IntegerField(default=0),
        ),
    ]
