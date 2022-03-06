from datetime import date

from django.test import TestCase

# Create your tests here.

#ls8
from . import models, forms

from django.test import Client
from django.contrib.auth.models import User

class ShowsTestModel(TestCase):

    def test_model_create_success(self):
        show = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "quantity": "25",
            "genre": "Comedy",
            "created_date": date.today(),
            "update_date": date.today(),
            "duration": 24,
        }
        shows = models.TVShow.objects.create(**show)
        self.assertEqual(shows.title, show["title"])
        self.assertEqual(shows.description, show["description"])
        self.assertEqual(shows.image, show["image"])
        self.assertEqual(shows.quantity, show["quantity"])
        self.assertEqual(shows.genre, show["genre"])
        self.assertEqual(shows.created_date, show["created_date"])
        self.assertEqual(shows.updated_date, show["updated_date"])
        self.assertEqual(shows.duration, show["duration"])
        # self.assertEqual(shows, show)
        # self.assertEqual(shows.title, "Test Title")

    def test_model_create_fail(self):
        show = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "quantity": "Long",
            "genre": "Comedy",
            # "created_date": date.today(),
            # "update_date": date.today(),
            "duration": 24,
        }
        with self.assertRaises(ValueError):
            shows = models.TVShow.objects.create(**show)

    def test_update_model(self):
        show = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "quantity": 25,
            "genre": "Comedy",
            "duration": 24,
        }
        shows = models.TVShow.objects.create(**show)
        new_title = "New Title"
        shows.title = new_title
        shows.save()
        shows.refresh_from_db()
        self.assertEqual(shows.title, new_title)

    def test_delete_model(self):
        show = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "quantity": 25,
            "genre": "Comedy",
            "duration": 24,
        }
        shows = models.TVShow.objects.create(**show)
        show_id = shows.id
        shows.delete()
        with self.assertRaises(models.TVShow.DoesNotExist):
            models.TVShow.objects.get(id=show_id)

class TestForm(TestCase):
    def test_form_create_success(self):
        show = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "quantity": 25,
            "genre": "Comedy",
            "created_date": date.today(),
            "update_date": date.today(),
            "duration": 24,
        }
        shows = models.TVShow.objects.create(**show)
        # data = {"shows": shows}
        # form = forms.TVShowForm(data)
        form = forms.TVShowForm(initial={"shows": shows})
        is_valid_form = form.is_valid()
        self.assertTrue(is_valid_form)
        # self.assertEqual(shows.title, show["title"])
        form.save()


class TestViews(TestCase):
    def test_get_success(self):
        show = {
            "title": "Test Title",
            "description": "Test Description",
            "image": "image.png",
            "quantity": 25,
            "genre": "Comedy",
            "duration": 24,
        }
        shows = models.TVShow.objects.create(**show)
        client = Client()
        user = User.objects.create(username='Username')
        client.force_login(user)
        response = client.get(path=f"/shows/{shows.id}/")
        self.assertEqual(response.status_code, 200)


