# Generated by Django 3.2.9 on 2021-12-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
