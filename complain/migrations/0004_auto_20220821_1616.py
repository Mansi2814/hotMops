# Generated by Django 2.2 on 2022-08-21 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0003_auto_20220821_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complainmodel',
            name='user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
