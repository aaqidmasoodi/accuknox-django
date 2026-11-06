from django.db import models


class Order(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.item
