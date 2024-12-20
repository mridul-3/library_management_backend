# Generated by Django 5.1.1 on 2024-10-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_user_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='issue_date',
        ),
        migrations.RemoveField(
            model_name='users',
            name='return_date',
        ),
        migrations.AddField(
            model_name='users',
            name='user_phone_no',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='books',
            name='publication_year',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
    ]
