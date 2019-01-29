# -*- coding: utf-8 -*-
""" Test configs """
from unittest import TestCase
from unittest.mock import patch

from phd import app


class WebAppTestCase(TestCase):
    def setUp(self):
        self.app = app.create_app().test_client()
        self.app.testing = True

    @patch("phd.web.app.db")
    def test_root(self, db):
        rv = self.app.get("/")
        self.assertEqual(302, rv.status_code)

    @patch("phd.web.app.db")
    def test_create_ingredient(self, db):
        rv = self.app.get("/create/ingredient/")
        self.assertEqual(302, rv.status_code)

    @patch("phd.web.app.db")
    def test_create_meal(self, db):
        rv = self.app.get("/create/meal/")
        self.assertEqual(302, rv.status_code)

    @patch("phd.web.app.db")
    def test_create_recipe(self, db):
        rv = self.app.get("/create/recipe/")
        self.assertEqual(302, rv.status_code)
