# Generated by Django 3.2.7 on 2021-09-20 06:39

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210919_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipevideo',
            name='link',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]