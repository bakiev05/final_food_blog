# Generated by Django 3.2.7 on 2021-09-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_recipevideo_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favourite',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image', verbose_name='Картинки'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
