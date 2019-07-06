#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:30:28 2019

@author: harish
@credits: http://jmrware.com/articles/2009/uri_regexp/URI_regex.html,
https://blog.mariam.dev/2016/10/13/murl-init.html,
https://github.com/venantius/takehome/tree/master/uriparse
This file contains all the regexes of URI and its constituents as per RFC 3986
"""

from uri_manipulator import UriHandler

DEMO_URI = r'https://scott:1234@drive.example.com/path/to/happiness.html?hello=world#go'
my_uri = UriHandler(DEMO_URI)
print(my_uri.authority)
print(my_uri.port)
