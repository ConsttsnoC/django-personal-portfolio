# Generated by Django 4.1.3 on 2022-12-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_images_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='data',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
    ]
