# URIManipulator
PREREQUISITES:
Python3+
packages:re,binascii

GENERAL USE:

create a UriHandler object using URI
foo=UriHandler('https://test.me?this=that')

or alternatively using
foo=UriHandler.from_uri_list(['https:','//test.me','','?this=that',''])   #list format - [scheme:, //authority, /path, ?query, #fragement]


ATTRIBUTES:

scheme,authority,path,query,fragment,port,host,userinfo

access these attributes of the class as follows
foo.scheme
foo.authority
..etc

METHODS:

append_query,update_query,update_schema,update_path,update_fragment

call these methods as follows
foo.append_query(query)
foo.update_schema(scheme)
..etc

Note:The methods automatically encodes the unsafe characters of the string before updating
Also there is no clear defenition for a domain name. Hence it is impossible to fetch the domain name from the hostname.However after going through some web articles I found a nice package called PublicSuffixList which extracts domain name from hostname from a public list, but the pitfall here is that the public list is exhaustive
