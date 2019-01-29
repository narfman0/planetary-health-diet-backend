# -*- coding: utf-8 -*-
""" Test configs """
from unittest import TestCase

from phd import log


class LogTestCase(TestCase):
    def test_create_logger(self):
        self.assertTrue(log.create_logger(__name__) is not None)
