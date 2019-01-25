# -*- coding: utf-8 -*-
""" Test configs """
from unittest import TestCase

from phd import wsgi


class WSGITestCase(TestCase):
    def test_wsgi(self):
        self.assertTrue(wsgi.app is not None)
