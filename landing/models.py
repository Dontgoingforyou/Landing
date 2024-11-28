from django.db import models


class SubmittedOrder(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"