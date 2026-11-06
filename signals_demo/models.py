from django.db import models


class Order(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.item


class SignalLog(models.Model):
    message = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.message
