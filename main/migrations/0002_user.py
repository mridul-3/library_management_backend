# Generated by Django 5.1.1 on 2024-10-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=30)),
                ('user_id', models.IntegerField(max_length=10)),
                ('issue_date', models.CharField(max_length=30)),
                ('return_date', models.CharField(max_length=30)),
            ],
        ),
    ]
