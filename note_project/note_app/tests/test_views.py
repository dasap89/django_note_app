# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from note_app.models import Note


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
        self.assertContains(response, "It is a note for testing purpose.")

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
        self.assertContains(response, "testing")
        self.assertContains(response, "Test")

