# Generated by Django 4.2 on 2023-06-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccessSystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='surename',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
