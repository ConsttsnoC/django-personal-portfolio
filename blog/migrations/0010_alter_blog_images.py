# Generated by Django 4.1.3 on 2022-12-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='images',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
    ]
