from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Title(models.Model):
    """A title that we will create for our post."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = " Titles"
class Notes(models.Model):
    """A class for creating a text"""
    name = models.ForeignKey(Title, on_delete=models.CASCADE)
    note = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Notes"
    def __str__(self):
        return f"{self.note[:50]}..."
