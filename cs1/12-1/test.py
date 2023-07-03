import re

def url_host(url):

     host_name = re.sub(r'(www\.[a-zA-z|[0-9]]+\.&org'),url)

     return host_name

print( url_host('https://www.iniad.org/en/access') )

print( url_host('http://moocs.iniad.org') )
