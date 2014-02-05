# -*- coding: utf-8 -*- 
'''
Created on 05-02-2014

@author: Tomek
'''

import urllib2
import urllib
class TextToAudioConverter(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.__google_url = u'http://translate.google.com/translate_tts?ie=UTF-8&tl=pl&q='
    
    def toMp3(self, text, file_url):
        text = urllib.quote_plus(text)
        url = self.__google_url + text
        request = urllib2.Request(url)
        request.add_header('User-agent', 'Mozilla/5.0') 
        opener = urllib2.build_opener()
        f = open(file_url, "wb")
        f.write(opener.open(request).read())
        f.close()