from django.db import models


class ShoppingItem(models.Model):

    name = models.CharField(max_length=60)
    quantity = models.PositiveSmallIntegerField()
    checked = models.BooleanField(default=False)
