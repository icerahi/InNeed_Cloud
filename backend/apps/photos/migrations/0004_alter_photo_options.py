# Generated by Django 3.2 on 2021-05-12 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-updated']},
        ),
    ]