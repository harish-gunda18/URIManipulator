#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:30:28 2019

@author: harish

"""
from uri_manipulator import UriHandler
DEC_OCTET = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
UNRESERVED = r'[A-Za-z0-9\-\.\_\~]'
GEN_DELIMS = r'[\:\/\?\#\[\]\@]'
SUB_DELIMS = r"[\!\$\&\'\(\)\*\+\,\;\=]"

DEMO_URI = r'https://scott:tiger@drive.example.com:123/path/to/happiness.html?hello=world#go'
my_uri = UriHandler(DEMO_URI)
print(my_uri.host)
