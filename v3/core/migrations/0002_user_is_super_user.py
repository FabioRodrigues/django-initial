# Generated by Django 3.0.6 on 2020-05-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_super_user',
            field=models.BooleanField(default=False),
        ),
    ]