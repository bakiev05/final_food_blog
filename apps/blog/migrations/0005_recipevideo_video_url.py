# Generated by Django 3.2.7 on 2021-09-19 18:11

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipevideo',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Видео_url_youtube'),
        ),
    ]