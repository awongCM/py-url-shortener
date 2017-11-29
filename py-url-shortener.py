
# Importing libraries
from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys

# Function call to make shortened urls
def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
    urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def main():
    urls = sys.argv[1:]

    for tinyurl in map(make_tiny, urls):
        print(tinyurl)

if __name__ == '__main__':
    main()


##TODO - Url Shortener using Redis/Python

# import redis

# r = redis.StrictRedis(host='localhost', port=6379, db=0)

# def shorten(self, long_url=None):
#     hashed_url = '%x' % self.r.incr('next.url.id')
#     self.r.set('url:%s:id' % hashed_url, long_url)
#     self.r.push('global:urls', hashed_url)
#     return hashed_url

# def expand(self, hashed_url):
#     return self.r.get('url:%s:id' % hashed_url)

# def visit(self, hashed_url=None, ip_address=None, agent=None, referrer=None):
#     visitorAgent = VisitorAgent(ip_address, agent, referrer)
#     self.r.push('visitors:%s:url' % hashed_url, json.dumps(visitorAgent))
#     return self.r.incr(clicks:%s:url % hashed_url)

# def clicks(self, hashed_url=None):
#     return self.r.get(self.URL_CLICKS_KEY % hashed_url)

# def recent_visitors(self, hashed_url=None):
#     visitorAgents = []
#     for v in self.r.lrange('visitors:%s:url' % hashed_url, 0, 10, 0):
#         visitorAgents.append(json.loads(v))
#     return visitorAgents

# def short_urls(self):
#     return self.r.lrange('global:urls', 0, 100)
