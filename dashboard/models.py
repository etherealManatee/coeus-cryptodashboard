from django.db import models
import uuid

# Create your models here.
class Instruments(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )