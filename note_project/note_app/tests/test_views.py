# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from ..models import Note


class TestViews(TestCase):

    fixtures = ['initial_data.json']

    def test_view_exist(self):
        """
        View should exist
        """
        response = self.client.get(reverse('note_app:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_with_initial_data(self):
        """
        View should response with initial data
        """
        response = self.client.get(reverse('note_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "It is a note loaded from fixtures.")

    def test_view_used_template(self):
        """
        Test that view for index page return template index.html in a response
        """
        response = self.client.get(reverse('note_app:index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_view_with_no_data(self):
        """
        Test if there is 0 rows in DB
        """
        Note.objects.all().delete()
        response = self.client.get(reverse('note_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no notes")
        self.assertEqual(len(response.context['object_list']), 0)

    def test_view_if_two_rows_in_db(self):
        """
        Test that view shows few notes
        """
        Note.objects.create(note_text="Test")
        response = self.client.get(reverse('note_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 2)
        self.assertContains(response, "fixture")
        self.assertContains(response, "Test")

    def test_view_check_templatetag(self):
        """
        Test that note is rendered with tamplatetag
        """
        response = self.client.get(reverse('note_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<li class=\"list-group-item\">")

    def test_view_note_cannot_be_add_with_invalid_data(self):
        """
        Test that data can't be added by NoteList with invalid data
        """
        before = Note.objects.all().count()
        response = self.client.get(reverse('note_app:index'))
        data = {'node_text': 'It\'s note'}
        response = self.client.post(
            reverse('note_app:index'),
            data,
        )
        self.assertEqual(response.status_code, 200)
        after = Note.objects.all().count()
        self.assertEqual(before, after)

    def test_view_note_can_be_added_with_valid_data(self):
        """
        Test that data can be added by NoteList with valid data
        """
        before = Note.objects.all().count()
        response = self.client.get(reverse('note_app:index'))
        data = {'note_text': 'It is a valid note.'}
        response = self.client.post(
            reverse('note_app:index'),
            data,
        )
        self.assertEqual(response.status_code, 200)
        after = Note.objects.all().count()
        self.assertNotEqual(before, after)
