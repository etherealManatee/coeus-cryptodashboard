# Generated by Django 3.2.5 on 2021-07-12 12:08

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('source', models.TextField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
