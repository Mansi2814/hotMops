# Generated by Django 2.2 on 2022-08-21 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0006_auto_20220821_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complainmodel',
            old_name='user_id',
            new_name='user',
        ),
    ]