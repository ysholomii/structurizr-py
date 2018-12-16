import unittest

from structurizr_py.core.util.url import Url


class TestUrl(unittest.TestCase):

    def test_is_url_returns_false_on_none(self):
        self.assertFalse(Url.is_url(None))

    def test_is_url_returns_false_on_empty_string(self):
        self.assertFalse(Url.is_url(""))
        self.assertFalse(Url.is_url(" "))

    def test_is_url_returns_false_on_invalid_url(self):
        self.assertFalse(Url.is_url("www.google.com"))
        self.assertFalse(Url.is_url("wwwgooglecom"))

    def test_is_url_returns_true_on_valid_url(self):
        self.assertTrue(Url.is_url("https://www.google.com"))
