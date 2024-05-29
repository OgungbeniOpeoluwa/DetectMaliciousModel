import unittest

from src import links, domains


class MyTestCase(unittest.TestCase):
    def test_replace_www(self):
        url = "https://www.google.com"
        expected = "https://.google.com"
        self.assertEqual(expected, links.replace_www(url))  # add assertion here

    def test_url_length(self):
        url = "https://www.google.com"
        expected = 1
        self.assertEqual(expected, links.have_ip_address(url))

    def test_abnormal_url(self):
        url = "br-icloud.com.br"
        expected = 0
        self.assertEqual(expected, links.abnormal_url(url))

    def test_url_region(self):
        url = "br-icloud.com.br"
        expected = "Brazil"
        self.assertEqual(expected, domains.get_url_region(url))

    def test_numeric_value(self):
        url = "https://www.example.com"
        print(links.numeric_value(url))


if __name__ == '__main__':
    unittest.main()
