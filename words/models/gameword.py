# Create your models here.
from django.db import models

from apps.words.models import Room


class GameWord(models.Model):
    name_of_gamer = models.CharField(max_length=100)
    word = models.CharField(max_length=40, blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Зв'язок ForeignKey

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.name_of_gamer} {self.word}"

    class Meta:
        ordering = ["-created_at", "name_of_gamer"]