# -*- encoding: utf-8 -*-
import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..forms import NoteForm


class Ticket_5_Tests_Form(TestCase):

    def test_edit_form_with_no_data(self):
        """
        Test that EditForm can't be empty
        """
        self.assertFalse(NoteForm(data={}).is_valid())

    def test_edit_form_with_invalid_data(self):
        """
        Test that EditForm is invalid when short text is
        given
        """
        data = {'node_text': 'It\'s note'}
        self.assertFalse(NoteForm(data=data).is_valid())

    def test_edit_form_with_valid_data(self):
        """
        Test that EditForm is valid with data that longer
        then 10 symbols
        """
        data = {'note_text': 'It is a valid note.'}
        self.assertTrue(NoteForm(data=data).is_valid())
