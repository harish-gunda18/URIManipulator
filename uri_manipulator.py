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
# Importing required packages
import binascii
import re

# URI regex as per RFC 3986 to extract various compnents of URI
# 1.schema:,2.schema,3.authority:,4.authority,5.path,6.?query,7.query,
# 8.#fragment,9.fragment
URI_REGEX = re.compile(
        r'^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')

# Authority patterns
USERINFO_PATTERN = re.compile(
        r"((?:[A-Za-z0-9\-._~!$&'()*+,;=:]|%[0-9A-Fa-f]{2})*)@")
PORT_PATTERN = re.compile(r":([0-9]+)$")

# REGEXES of components(R is short for REGEX)
QUERY_R = re.compile('|'.join([r'[A-Za-z0-9\-\.\_\~]',
                               r"[\!\$\&\'\(\)\*\+\,\;\=]",
                               r'[\:\@]', r'[\/\?]']))
PATH_R = re.compile('|'.join([r'[A-Za-z0-9\-\.\_\~]',
                              r"[\!\$\&\'\(\)\*\+\,\;\=]",
                              r'[\:\@]']))
FRAGMENT_R = QUERY_R


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

    @classmethod
    def from_uri_list(cls, uri_list):
        """
        returns an uri object
        e.g : x = UriHandler.from_uri_list(uri_list)

        Args:
            uri_list: [schema,authority,path,query,fragement]
        """
        uri = ''.join(uri_list)
        return cls(uri)

    @property
    def schema(self):
        if self.uri_components_list[1] == '':
            return None
        return self.uri_components_list[1]

    @property
    def authority(self):
        if self.uri_components_list[3] == '':
            return None
        return self.uri_components_list[3]

    @property
    def path(self):
        if self.uri_components_list[4] == '':
            return None
        return self.uri_components_list[4]

    @property
    def querystring(self):
        if self.uri_components_list[6] == '':
            return None
        return self.uri_components_list[6]

    @property
    def fragment(self):
        if self.uri_components_list[8] == '':
            return None
        return self.uri_components_list[8]

    @property
    def port(self):
        port_tuple = re.findall(PORT_PATTERN, self.authority)
        if port_tuple != []:
            return int(port_tuple[0])
        return None

    @property
    def userinfo(self):
        userinfo_tuple = re.findall(USERINFO_PATTERN, self.authority)
        if userinfo_tuple != []:
            return userinfo_tuple[0]
        return None

    @property
    def host(self):
        if self.userinfo is not None:
            if self.port is not None:
                return self.authority.split('@')[1].split(':')[0]
            else:
                return self.authority.split('@')[1]
        else:
            if self.port is None:
                return self.authority
            else:
                return self.authority.split(':')[0]
        

    def append_query(self, append_query):
        """
        appends query variable to append query with encoding

        Args:
            append_query: string to append
        """
        append_query = self.encode(QUERY_R, append_query)
        if self.querystring is not None:
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
        updates query variable to update_query with encoding

        Args:
            update_query: string to update
        """
        update_query = self.encode(QUERY_R, update_query)
        self.uri_components_list[5] = '?' + update_query
        self.uri_components_list[6] = update_query
        self.uri = self.uri_builder()

    def encode(self, regex, string):
        """
        encodes string with the given regex(allowed chars)

        Args:
            regex: allowed chars
            string: string
        """
        return ''.join(['%' + str(binascii.hexlify(bytes(x, 'utf-8')), 'ascii')
                        if not regex.search(x) else x for x in string])

    def update_schema(self, new_schema):
        """
        updates schema to new_schema

        Args:
            new_schema: schema to update
        """
        self.uri_components_list[0] = new_schema + ':'
        self.uri_components_list[1] = new_schema
        self.uri = self.uri_builder()

    def update_path(self, new_path):
        """
        updates path to new_path with encoding

        Args:
            new_path: path to update
        """
        new_path = self.encode(PATH_R, new_path)
        self.uri_components_list[4] = new_path
        self.uri = self.uri_builder()

    def update_fragment(self, new_fragment):
        """
        updates fragment to new_fragment with encoding

        Args:
            new_fragment: fragment to update
        """
        new_fragment = self.encode(FRAGMENT_R, new_fragment)
        self.uri_components_list[7] = '#' + new_fragment
        self.uri_components_list[8] = new_fragment
        self.uri = self.uri_builder()
