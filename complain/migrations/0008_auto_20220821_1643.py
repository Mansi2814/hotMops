# Generated by Django 2.2 on 2022-08-21 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0007_auto_20220821_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complainmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]