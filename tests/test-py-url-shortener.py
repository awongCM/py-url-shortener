#TODO - UNIT TESTING

import unittest

from py-url-shortener import UrlShortenerService, url_string_formatter,
                        encode_base64, decode_base64
 
class TestUM(unittest.TestCase):
 
    def main(self):
         # inistantiate url_shorteer_service
        url_shortener_service = UrlShortenerService()

        #read text input file
        readInputFile('urls-to-read.txt', url_shortener_service)

        #Web visitor activity being tracking...
        visitors_visiting(url_shortener_service)

def readInputFile(text_file, url_shortener_service):
    with open(text_file, 'r') as infile:
        for line in infile:
            # Ignore any comments in file
            if '#' not in line[0]:
                shortened_url, encoded_url = url_shortener_service.shorten_url(line)

                expanded_url = url_shortener_service.expand_url(encoded_url)

                print("ShortenedURL: {0}; ExpandedURL: {1}".format(shortened_url, expanded_url))
                
    return

def visitors_visiting(url_shortener_service):

    print('Visitors visiting...')

    for i in range(0, 5):    
        for d in url_shortener_service.short_urls():
            decoded_url = decode_base64(d)
            print('... %s' % decoded_url)
            url_shortener_service.visit(decoded_url)

    print('Recent Visitors')

    for d in url_shortener_service.short_urls():
        expanded_url = url_shortener_service.expand_url(d)
        decoded_url = decode_base64(d)
        print('... %s' % decoded_url)
        visitor_agents = url_shortener_service.recent_visitors(decoded_url)
        print('Total recent vistors for {0} (ie {1}) are {2}'.format(decoded_url, expanded_url, len(visitor_agents)))

    return


if __name__ == '__main__':
    unittest.main()