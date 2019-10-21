from urllib.parse import urlsplit
import unittest
import requests


class PagesTestCase(unittest.TestCase):
    def test_http_redirect_to_https(self):
        response = requests.get('http://fmartingr.com', allow_redirects=False)
        scheme, host, *_ = urlsplit(response.headers.get("Location"))
        self.assertEqual(response.status_code, 301)
        self.assertEqual(scheme, 'https')
        self.assertEquals(host, "fmartingr.com")

    def test_www_redirects_to_non_www(self):
        response = requests.get('https://www.fmartingr.com', allow_redirects=False)
        scheme, host, *_ = urlsplit(response.headers.get("Location"))
        self.assertEqual(response.status_code, 301)
        self.assertEqual(scheme, 'https')
        self.assertEquals(host, "fmartingr.com")
