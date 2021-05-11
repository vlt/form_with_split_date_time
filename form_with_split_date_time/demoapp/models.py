import datetime

from django.db import models


class Universe(models.Model):
    begin = models.DateTimeField(
        default=datetime.datetime.now,
    )

    def __str__(self):
        return f"{self.pk}: {self.begin}"
