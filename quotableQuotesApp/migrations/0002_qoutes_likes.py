# Generated by Django 2.2 on 2020-01-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotableQuotesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoutes',
            name='likes',
            field=models.ManyToManyField(related_name='comment_liked', to='quotableQuotesApp.User'),
        ),
    ]