# Generated by Django 4.1.3 on 2022-11-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogproject_my_field_name_blogproject_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogproject',
            name='descriptoin',
            field=models.CharField(max_length=250, null=True),
        ),
    ]