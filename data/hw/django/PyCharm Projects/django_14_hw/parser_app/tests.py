from django.test import TestCase

# Create your tests here.
#hw8
from . import models, forms
from django.test import Client
from django.contrib.auth.models import User

class TestParserModel(TestCase):
    def test_model_parser_create_success(self):
        parser = {
            "title": "Test Title",
            "image": "image.png",
        }
        parser_app = models.PaymentCard.objects.create(**parser)
        self.assertEqual(parser_app.title, parser["title"])
        self.assertEqual(parser_app.image, parser["image"])


    def test_model_parser_create_fail(self):
        parser = {
            "title": 25,
            "image": "image.png",
        }
        with self.assertRaises(ValueError):
            parser_app = models.PaymentCard.objects.create(**parser)



class TestParserForm(TestCase):
    def test_form_parser_create_success(self):
        parser = {
            "title": "Test Title",
            "image": "image.png",
        }
        parser_app = models.PaymentCard.objects.create(**parser)
        form = forms.ParserForm(initial={"parser": parser_app})
        is_valid_form = form.is_valid()
        self.assertTrue(is_valid_form)
        form.save()

    def test_form_parser_create_fail(self):
        parser = {
            "title": "Test Title",
            "image": "image.png",
        }
        with self.assertRaises(ValueError):
            parser_app = models.PaymentCard.objects.create(**parser)
            form = forms.ParserForm(initial={"parser": parser_app})
            is_valid_form = form.is_valid()
            self.assertTrue(is_valid_form)
            form.save()


class TestParserViews(TestCase):
    def test_view_parser_success(self):
        parser = {
            "title": "Test Title",
            "image": "image.png",
        }
        parser_app = models.PaymentCard.objects.create(**parser)
        client = Client()
        user = User.objects.create(username='Username')
        client.force_login(user)
        response = client.get(path=f"/card/{parser_app.id}/")
        self.assertEqual(response.status_code, 200)

    def test_view_parser_fail(self):
        parser = {
            "title": "Test Title",
            "image": "image.png",
        }
        with self.assertRaises(ValueError):
            parser_app = models.PaymentCard.objects.create(**parser)
            client = Client()
            user = User.objects.create(username='Username')
            client.force_login(user)
            response = client.get(path=f"/card/{parser_app.id}/")
            self.assertEqual(response.status_code, 200)

