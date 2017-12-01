# TODOs - to place in a setup folder
# Importing libraries
# from __future__ import print_function
from math import floor

import string
import random
import pdb
import sys
import base64

# Basic implementation of shortened urls
def shorten_url(url):
    # jumbled them
    prefix_url = 'http://rllytny.url/'

    url_str_arr = list(url)
    random.shuffle(url_str_arr)
    
    # get the last 10 items of the jumbled_url, assuming url is very longer than 20 chars
    if len(url_str_arr) > 20:
        shortened_url = url_str_arr[-10:]
    else:
        shortened_url = url_str_arr

    jumbled_url = ''.join(shortened_url)

    hashed_url = prefix_url + jumbled_url

    encoded_url = encodeBase64(jumbled_url)
    decoded_url = decodeBase64(encoded_url)

    return hashed_url, url, encoded_url, decoded_url

#  Base64 Encoding/Decoding functions
def encodeBase64(toencode):    
    result = base64.b64encode(toencode)
    return result

def decodeBase64(todecode):
    result = base64.b64decode(todecode)
    return result

def readInputFile(text_file):
    with open(text_file, 'r') as infile:
        for line in infile:
            # Ignore any comments in file
            if '#' not in line[0]:
                # print("URL read: {0}".format(line))
                shortened_url, raw_url, encoded_url, decoded_url = shorten_url(line)
                print("OriginalURL: {0}, NewURL: {1}, EncodedURL: {2}, DecodedURL: {3}".format(raw_url, shortened_url, encoded_url, decoded_url))
                sys.stdout.write('.')
    return

def main():
    urls = sys.argv[1:]

    #print out their respective encoded and decoded strings
    # for shortened_url, raw_url, encoded_url, decoded_url in map(shorten_url, urls):
    #     print("Original url: {0}, Shortened url: {1}, EncodedURL: {2}, DecodedURL: {3}".format(raw_url, shortened_url, encoded_url, decoded_url))

    #read text input file
    readInputFile('urls-to-read.txt')

if __name__ == '__main__':
    main()


##TODO - Next Build Url Shortener Service using Redis/Python

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
