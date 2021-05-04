# Generated by Django 2.2 on 2021-04-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title_de',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
