from django.db import models

class AirportRoute(models.Model):
    airport_code = models.CharField(max_length=10)
    position = models.CharField(
        max_length=10,
        choices=[('Left', 'Left'), ('Right', 'Right')]
    )
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return f"{self.airport_code} - {self.position} - {self.duration} mins"
