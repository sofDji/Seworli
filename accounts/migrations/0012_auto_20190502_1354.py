# Generated by Django 2.2 on 2019-05-02 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_user_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='interests',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
