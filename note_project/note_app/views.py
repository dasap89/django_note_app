from django.views.generic import ListView
from . models import Note
from . forms import NoteForm
from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render


class NoteList(FormMixin, ListView):
    model = Note
    template_name = "index.html"
    form_class = NoteForm

    def get_queryset(self):
        queryset = super(NoteList, self).get_queryset()
        self.form = NoteForm()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NoteList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()

        else:
            note_list = Note.objects.all()
            return render(
                request,
                'index.html',
                {'object_list': note_list, 'form': self.form}
            )
        return self.get(request, *args, **kwargs)
