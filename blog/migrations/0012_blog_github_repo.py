# Generated by Django 4.1.3 on 2023-02-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='github_repo',
            field=models.URLField(blank=True),
        ),
    ]