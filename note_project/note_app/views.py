from django.views.generic import ListView
from . models import Note

class NoteList(ListView):
    model = Note
    context_object_name = 'list_of_notes'
    template_name = 'index.html'
