from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)  # short title for the note
    content = models.TextField()              # main content of the note
    created_at = models.DateTimeField(auto_now_add=True)  # set once when created
    updated_at = models.DateTimeField(auto_now=True)      # updates every time saved

    def __str__(self):
        return self.title
