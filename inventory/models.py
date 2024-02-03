from django.db import models


class Warehouse(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=30,
        blank=False,
    )
    quantity = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.name
