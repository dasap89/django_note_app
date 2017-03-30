from django.db import models


class Note(models.Model):
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return note_text
