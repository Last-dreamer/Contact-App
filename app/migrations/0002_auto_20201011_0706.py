# Generated by Django 3.1.2 on 2020-10-11 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user',
            new_name='manager',
        ),
    ]
