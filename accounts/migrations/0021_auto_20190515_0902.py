# Generated by Django 2.2 on 2019-05-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_user_yanotif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='yanotif',
            field=models.BooleanField(default=False),
        ),
    ]
