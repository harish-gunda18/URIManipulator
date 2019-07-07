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
        self.google_case = UriHandler("https://user:password@www.google.com"
                                      ":123/search?q=setter+python&oq=setter"
                                      "+python&aqs=chrome..69i57j0l3.9438j0&"
                                      "sourceid=chrome&ie=UTF-8#hello")
        # alternate object creation case with all components
        self.google_list_case = \
            UriHandler.from_uri_list(
                ['https:', '//user:password@www.google.com:123', '/search',
                 '?q=setter+python&oq=setter+python&aqs=chrome..69i57j0l3.'
                 '9438j0&sourceid=chrome&ie=UTF-8', '#hello'])

    def test_scheme(self):
        """
        testing if scheme is parsed properly
        """
        self.assertEqual(self.google_case.schema, 'https')
        self.assertEqual(self.google_list_case.schema, 'https')

    def test_authority(self):
        """
        testing if authority is parsed properly
        """
        self.assertEqual(self.google_case.authority, "user:password@www.google"
                         ".com:123")
        self.assertEqual(self.google_list_case.authority, "user:password@"
                         "www.google.com:123")

    def test_path(self):
        """
        testing if path is parsed properly
        """
        self.assertEqual(self.google_case.path, '/search')
        self.assertEqual(self.google_list_case.path, '/search')

    def test_querystring(self):
        """
        testing if querystring is parsed properly
        """
        self.assertEqual(self.google_case.querystring, "q=setter+python&oq="
                         "setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid="
                         "chrome&ie=UTF-8")
        self.assertEqual(self.google_list_case.querystring, "q=setter+python&o"
                         "q="
                         "setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid="
                         "chrome&ie=UTF-8")

    def test_fragment(self):
        """
        testing if fragment is parsed properly
        """
        self.assertEqual(self.google_case.fragment, 'hello')
        self.assertEqual(self.google_list_case.fragment, 'hello')

    def test_port(self):
        """
        testing if port is parsed properly
        """
        self.assertEqual(self.google_case.port, 123)
        self.assertEqual(self.google_list_case.port, 123)

    def test_userinfo(self):
        """
        testing if userinfo is parsed properly
        """
        self.assertEqual(self.google_case.userinfo, 'user:password')
        self.assertEqual(self.google_list_case.userinfo, 'user:password')

    def test_host(self):
        """
        testing if host is parsed properly
        """
        self.assertEqual(self.google_case.host, 'www.google.com')
        self.assertEqual(self.google_list_case.host, 'www.google.com')

    def test_append_query(self):
        """
        testing if append_query is working properly
        """
        self.google_case.append_query('foo=bar')
        self.assertEqual(self.google_case.querystring, "q=setter+python&oq="
                         "setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid="
                         "chrome&ie=UTF-8&foo=bar")
        self.google_list_case.append_query('foo=bar')
        self.assertEqual(self.google_list_case.querystring, "q=setter+python&o"
                         "q="
                         "setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid="
                         "chrome&ie=UTF-8&foo=bar")

    def test_update_query(self):
        """
        testing if update_query is working properly
        """
        self.google_case.update_query('foo=bar')
        self.assertEqual(self.google_case.querystring, 'foo=bar')
        self.google_list_case.update_query('foo=bar')
        self.assertEqual(self.google_list_case.querystring, 'foo=bar')

    def test_update_schema(self):
        """
        testing if update_schema is working properly
        """
        self.google_case.update_schema('http')
        self.assertEqual(self.google_case.schema, 'http')
        self.google_list_case.update_schema('http')
        self.assertEqual(self.google_list_case.schema, 'http')

    def test_update_path(self):
        """
        testing if update_path is working properly
        """
        self.google_case.update_path('/root')
        self.assertEqual(self.google_case.path, '/root')
        self.google_list_case.update_path('/root')
        self.assertEqual(self.google_list_case.path, '/root')

    def test_update_fragment(self):
        """
        testing if update_fragment is working properly
        """
        self.google_case.update_fragment('bye')
        self.assertEqual(self.google_case.fragment, 'bye')
        self.google_list_case.update_fragment('bye')
        self.assertEqual(self.google_list_case.fragment, 'bye')


if __name__ == "__main__":

    unittest.main()
