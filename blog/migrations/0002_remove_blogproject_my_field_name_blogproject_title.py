# Generated by Django 4.1.3 on 2022-11-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogproject',
            name='my_field_name',
        ),
        migrations.AddField(
            model_name='blogproject',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
