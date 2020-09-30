from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=False)
    createdBy = models.ForeignKey(
        User, verbose_name="Creator",
        on_delete=models.CASCADE, editable=False, null=True, blank=False)

    timeStamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.name
