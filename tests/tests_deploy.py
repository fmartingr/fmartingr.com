import unittest

import requests


class DeployTestCase(unittest.TestCase):
    def test_http_redirect_to_https(self):
        result = requests.get('http://fmartingr.com', allow_redirects=False)
        self.assertEqual(result.status_code, 301)
        self.assertEqual(result.headers.get('Location'),
                          'https://fmartingr.com/')

    def test_www_redirects_to_non_www(self):
        request = requests.get('https://www.fmartingr.com',
                               allow_redirects=False)
        self.assertEqual(request.status_code, 301)
        self.assertEqual(request.headers.get('Location'),
                          'https://fmartingr.com/')
