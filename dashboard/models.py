from django.db import models
from accounts.models import User
import uuid
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Cryptocurrency(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200, default="")
    api_id = models.IntegerField(default=0)
    

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="cryptocurrencies")

class Dashboard(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    # crypto_id = models.IntegerField()
    # name = models.CharField(max_length=200)
    # pos = ArrayField()
    # [{name: "", pos: ""}]
    # ["bitcoin", "eth", ""]
    pos  = ArrayField(models.CharField(max_length=50))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="dashboard_setup")