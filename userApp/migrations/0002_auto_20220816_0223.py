# Generated by Django 2.2 on 2022-08-15 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccountmodel',
            old_name='user_account_object',
            new_name='user',
        ),
    ]