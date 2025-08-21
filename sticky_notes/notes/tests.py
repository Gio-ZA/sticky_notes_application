from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    def test_create_note(self):
        note = Note.objects.create(title="Test Note", content="This is a test note.")
        self.assertEqual(str(note), "Test Note")
        self.assertEqual(note.content, "This is a test note.")

class NoteViewsTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Sample Note", content="Sample content")

    def test_list_view(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Note")
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_detail_view(self):
        response = self.client.get(reverse("note_detail", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample content")
        self.assertTemplateUsed(response, "notes/note_detail.html")

    def test_create_view(self):
        response = self.client.post(reverse("note_create"), {
            "title": "New Note",
            "content": "New content"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Note.objects.last().title, "New Note")

    def test_update_view(self):
        response = self.client.post(reverse("note_update", args=[self.note.id]), {
            "title": "Updated Note",
            "content": "Updated content"
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Note")

    def test_delete_view(self):
        response = self.client.post(reverse("note_delete", args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
