from django.db import models


class Room(models.Model):
    name_of_room = models.CharField(max_length=100)

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"#{self.pk} {self.name_of_room}"

    class Meta:
        ordering = ["-created_at", "pk"]


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
