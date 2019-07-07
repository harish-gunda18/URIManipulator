#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:30:28 2019

@author: harish

"""
from uri_manipulator import UriHandler

DEMO_URI = r'https://www.google.com:123/search?q=setter+python&oq=setter+python&aqs=chrome..69i57j0l3.9438j0&sourceid=chrome&ie=UTF-8'
#my_uri = UriHandler(DEMO_URI)
my_uri = UriHandler.from_uri_list(['https:','//www.google.com','/search','?q=setter',''])
print(my_uri.uri_components_list)
print(my_uri.schema)
print(my_uri.authority)
print(my_uri.path)
print(my_uri.querystring)
print(my_uri.fragment)
print(my_uri.port)
print(my_uri.userinfo)
print(my_uri.host)
print('updating query')
my_uri.update_query('foo=bar')
print(my_uri.querystring)

