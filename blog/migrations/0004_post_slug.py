# Generated by Django 5.1.1 on 2024-10-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='example-slug', unique=True),
            preserve_default=False,
        ),
    ]
