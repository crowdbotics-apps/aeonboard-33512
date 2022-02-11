from django.conf import settings
from django.db import models


class FlashCards(models.Model):
    "Generated Model"
    front = models.TextField()
    back = models.TextField()
