# Generated by Django 5.1.3 on 2024-11-11 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_participant_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='user',
        ),
    ]