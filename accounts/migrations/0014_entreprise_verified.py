# Generated by Django 2.2 on 2019-05-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20190507_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
