# Generated by Django 3.2.5 on 2021-07-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210714_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrency',
            name='symbol',
            field=models.CharField(default='', max_length=200),
        ),
    ]
