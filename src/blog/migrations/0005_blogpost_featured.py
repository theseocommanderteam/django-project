# Generated by Django 3.2.7 on 2023-03-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
