# Generated by Django 4.1.6 on 2023-02-09 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_member_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='role',
        ),
        migrations.AddField(
            model_name='member',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
