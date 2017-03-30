from django import forms
from . models import Note


class NoteForm(forms.ModelForm):
    note_text = forms.CharField(
        min_length=10,

    )

    class Meta:
        model = Note
        fields = ['note_text', ]
