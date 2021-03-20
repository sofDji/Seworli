# Generated by Django 2.2 on 2019-05-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espaces_partage', '0002_auto_20190525_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'photo', 'verbose_name_plural': 'photos'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]