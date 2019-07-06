# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Thu Jul  4 19:30:28 2019

@author: harish

@credits: http://jmrware.com/articles/2009/uri_regexp/URI_regex.html,
https://blog.mariam.dev/2016/10/13/murl-init.html,
https://github.com/venantius/takehome/tree/master/uriparse
This file contains URI and its constituents as per RFC 3986
"""

import re

# URI regex as per RFC 3986
URI_REGEX = re.compile(
        r'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')

DEC_OCTET = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
UNRESERVED = r'[A-Za-z0-9\-\.\_\~]'
GEN_DELIMS = r'[\:\/\?\#\[\]\@]'
SUB_DELIMS = r"[\!\$\&\'\(\)\*\+\,\;\=]"

# Authority regexes
USERINFO_REGEX = re.compile(
        r"(?:[A-Za-z0-9\-._~!$&'()*+,;=:]|%[0-9A-Fa-f]{2})*")
PORT_REGEX = re.compile(r":([0-9]+$)")


class UriHandler:

    def __init__(self, uri):
        self.uri = uri
        self.uri_components_list = re.findall(URI_REGEX, uri)[0]
        self.schema = self.uri_components_list[1]
        self.authority = self.uri_components_list[3]
        self.path = self.uri_components_list[3]
        self.querystring = self.uri_components_list[6]
        self.fragment = self.uri_components_list[8]
# =============================================================================
#     def get_schema(self):
#         return self.schema
#     
#     
#     def get_authority(self):
#         return self.authority
#     
#     
#     def get_path(self):
#         return self.path
#     
#     
#     def get_querystring(self):
#         return self.querystring
#     
#     
#     def get_fragment(self):
#         return self.fragment
# =============================================================================  
    @property
    def port(self):
        a = re.findall(PORT_REGEX, self.authority)[0]
        if a != []:
            return a
        return ''

    @property
    def userinfo(self):
        a = re.findall(USERINFO_REGEX, self.authority)[0]
        if a != []:
            return a
        return ''
