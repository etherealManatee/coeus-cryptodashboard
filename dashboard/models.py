from django.db import models
from accounts.models import User
import uuid

# Create your models here.
class Instruments(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=200)
    source = models.TextField()

    user = models.ManyToManyField(User, name="user")

class Cryptocurrency(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=20)


    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="cryptocurrencies")