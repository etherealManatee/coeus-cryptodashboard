# Generated by Django 3.2.5 on 2021-07-15 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
    ]
