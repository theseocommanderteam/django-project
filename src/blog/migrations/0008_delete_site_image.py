# Generated by Django 3.2.7 on 2023-03-28 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_site_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='site_image',
        ),
    ]