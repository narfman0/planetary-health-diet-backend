# -*- coding: utf-8 -*-
""" Test configs """
from unittest import TestCase
from unittest.mock import patch, MagicMock

from phd import db


class MockDict(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.id = kw["id"]


class DBTestCase(TestCase):
    @patch("phd.db.datastore")
    def test_get_entities(self, datastore):
        client = MagicMock()
        query = MagicMock()
        client.query.return_value = query
        query.fetch.return_value = [
            MockDict(id=1, name="entity1"),
            MockDict(id=2, name="entity2"),
        ]
        datastore.Client.return_value = client
        entities = db.get_entities("kind1")
        self.assertEqual(2, len(entities))

    @patch("phd.db.datastore")
    def test_put_entity(self, datastore):
        client = MagicMock()
        datastore.Client.return_value = client
        db.put_entity("kind1", {"name": "entity"})
        self.assertTrue(client.put.called)
