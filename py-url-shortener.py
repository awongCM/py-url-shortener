# TODOs - to place in a setup folder
# Importing libraries
import string
import random
import redis
import sys
import base64
import json

# instantiate the local resider server
redis_srv = redis.StrictRedis(host='localhost', port=6379, db=0)

# global variables - if any

# Actionable methods
def shorten_url(long_url):
    # jumbled them
    prefix_url = 'http://rllytny.url/'

    url_str_arr = list(long_url)
    random.shuffle(url_str_arr)
    
    # get the last 10 items of the jumbled_url, assuming url is very longer than 20 chars
    if len(url_str_arr) > 20:
        shortened_url = url_str_arr[-10:]
    else:
        shortened_url = url_str_arr

    jumbled_url = ''.join(shortened_url)

    shortened_url = prefix_url + jumbled_url

    encoded_url = encode_base64(jumbled_url)
    decoded_url = decode_base64(encoded_url)

    redis_srv.set('shortened.url:%s' % shortened_url, long_url)
    redis_srv.lpush('global:urls', shortened_url)

    return shortened_url, long_url, encoded_url, decoded_url

def expand_url(shortened_url):
    return redis_srv.get('shortened.url:%s' % shortened_url)

def visit(shortened_url=None, ip_address=None, agent=None, referrer=None):
    visitorAgent = {'ip_address': ip_address, 'agent':agent, 'referrer':referrer}
    redis_srv.lpush('visitors:%s:url' % shortened_url, json.dumps(visitorAgent))
    return redis_srv.incr('clicks:%s:url' % shortened_url)

# Retrieve counter properties from Redis
def clicks(shortened_url = None):
    return redis_srv.get('clicks:%s:url' % shortened_url)

def recent_visitors(shortened_url):
    visitorAgents = []
    for v in redis_srv.lrange('visitors:%s:url' % shortened_url, 0, -1):
        visitorAgents.append(json.loads(v))
    return visitorAgents

def short_urls():
    return redis_srv.lrange('global:urls', 0, 100)


#  Base64 Encoding/Decoding functions
def encode_base64(toencode):    
    result = base64.b64encode(toencode)
    return result

def decode_base64(todecode):
    result = base64.b64decode(todecode)
    return result

def readInputFile(text_file):
    with open(text_file, 'r') as infile:
        for line in infile:
            # Ignore any comments in file
            if '#' not in line[0]:
                shortened_url, raw_url, encoded_url, decoded_url = shorten_url(line)
                expanded_url = expand_url(shortened_url)

                print("OriginalURL: {0}, NewURL: {1}, EncodedURL: {2}, DecodedURL: {3}".format(raw_url, shortened_url, encoded_url, decoded_url))
                sys.stdout.write('.')
    return

def visitors_visiting():

    print('Visitors visiting...')

    for i in range(0, 5):    
        for d in short_urls():
            print('... %s' % d)
            visit(d)

    print('Recent Visitors')

    for d in short_urls():
        print('... %s' % d)
        visitor_agents = recent_visitors(d)
        print('Total recent vistors for {0} are {1}'.format(d, len(visitor_agents)))

    return

def main():
    urls = sys.argv[1:]

    #read text input file
    readInputFile('urls-to-read.txt')

    #Web visitor activity being tracking...
    visitors_visiting()

if __name__ == '__main__':
    main()