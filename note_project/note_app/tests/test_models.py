# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from note_app.models import Note


class TestModels(TestCase):

    fixtures = ['initial_data.json']

    def test_model_exist_with_no_data(self):
        """
        Test that model exists in DB
        """
        old_data = Note.objects.all().delete()
        data_in_model = Note.objects.all()
        self.assertEqual(len(data_in_model), 0)

    def test_model_can_store_data(self):
        """
        Test that model can stores new entry and shows two notes
        """
        Note.objects.create(note_text="Test")
        data_in_model = Note.objects.all().count()
        self.assertEqual(data_in_model, 2)

