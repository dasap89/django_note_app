from django import template
from note_app.models import Note
from django.template import TemplateSyntaxError
from copy import copy

register = template.Library()

@register.inclusion_tag('one_note.html', takes_context=True)
def show_one_note(context, note_id):
    
    try:
    	note = Note.objects.get(pk=note_id)
    except:
    	raise TemplateSyntaxError("'show_one_content' received invalid argument. It should be id of note.")

    context = copy(context)
    
    context.update({
	'note': note
    })

    return context
