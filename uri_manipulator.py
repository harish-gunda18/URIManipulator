# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Thu Jul  4 19:30:28 2019

@author: harish

@credits: http://jmrware.com/articles/2009/uri_regexp/URI_regex.html,
https://blog.mariam.dev/2016/10/13/murl-init.html,
https://github.com/venantius/takehome/tree/master/uriparse
This file contains URIHandler class and its constituents as per RFC 3986
"""

import re

# URI regex as per RFC 3986
URI_REGEX = re.compile(
        r'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')

# Authority patterns
USERINFO_PATTERN = re.compile(
        r"((?:[A-Za-z0-9\-._~!$&'()*+,;=:]|%[0-9A-Fa-f]{2})*)@")
PORT_PATTERN = re.compile(r":([0-9]+$)")


class UriHandler:

    def __init__(self, uri):
        """
        returns an uri object
        e.g : x = UriHandler(uri)

        Args:
            uri: uri string
        """
        self.uri = uri
        self.uri_components_list = list(re.findall(URI_REGEX, uri)[0])

    @property
    def schema(self):
        return self.uri_components_list[1]

    @property
    def authority(self):
        return self.uri_components_list[3]

    @property
    def path(self):
        return self.uri_components_list[3]

    @property
    def querystring(self):
        return self.uri_components_list[6]

    @property
    def fragment(self):
        return self.uri_components_list[8]

    @property
    def port(self):
        port_tuple = re.findall(PORT_PATTERN, self.authority)
        if port_tuple != []:
            return port_tuple[0]
        return ''

    @property
    def userinfo(self):
        userinfo_tuple = re.findall(USERINFO_PATTERN, self.authority)
        if userinfo_tuple != []:
            return userinfo_tuple[0]
        return ''

    @property
    def host(self):
        if self.userinfo == '':
            return self.authority
        if self.port == '':
            return self.authority.split('@')[1]
        return self.authority.split('@')[1].split(':')[0]

    def append_query(self, append_query):
        """
        appends query variable to append query

        Args:
            append_query: string to append
        """
        if self.querystring != '':
            self.uri_components_list[5] = self.uri_components_list[5] + '&' \
                + append_query
            self.uri_components_list[6] = self.uri_components_list[6] + '&' \
                + append_query
        self.uri = self.uri_builder()

    def uri_builder(self):
        """
        combines modified elements into a uri string
        """
        return self.uri_components_list[0] + self.uri_components_list[2] + \
            self.uri_components_list[4] + self.uri_components_list[5] + \
            self.uri_components_list[7]

    def update_query(self, update_query):
        """
        appends query variable to append query

        Args:
            update_query: string to update
        """
        self.uri_components_list[5] = '?' + update_query
        self.uri_components_list[6] = update_query
        self.uri = self.uri_builder()
