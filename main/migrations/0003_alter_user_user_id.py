# Generated by Django 5.1.1 on 2024-10-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
