from django.db import models


class ControlLamp(models.Model):
    TURN_CHOICES = (
        ('1', 'On'),
        ('0', 'Off')
    )
    state = models.CharField(max_length=1, choices=TURN_CHOICES, blank=False, default='0')

    def __str__(self):
        return str(self.pk)
