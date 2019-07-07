#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:30:28 2019

@author: harish

"""
from uri_manipulator import UriHandler
import unittest


class TestUri(unittest.TestCase):

    def setUp(self):
        """
        defining all the test cases
        """
        # has all the components
        self.google_case = UriHandler(r'https://user:password@www.google.com:123/search?q=setter+python&oq=setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid=chrome&ie=UTF-8#hello')

    def test_scheme(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.schema, 'https')

    def test_authority(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.authority, 'user:password@www.google.com:123')

    def test_path(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.path, '/search')

    def test_querystring(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.querystring, 'q=setter+python&oq=setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid=chrome&ie=UTF-8')

    def test_fragment(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.fragment, 'hello')

    def test_port(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.port, 123)

    def test_userinfo(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.userinfo, 'user:password')

    def test_host(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.host, 'www.google.com')


if __name__ == "__main__":
    unittest.main()
