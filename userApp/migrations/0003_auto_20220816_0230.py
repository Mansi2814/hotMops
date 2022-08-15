# Generated by Django 2.2 on 2022-08-15 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20220816_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccountmodel',
            name='user',
        ),
        migrations.AlterField(
            model_name='useraccountmodel',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
