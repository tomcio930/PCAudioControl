## -*- coding: utf-8 -*- 
#import urllib2
#import urllib
#import mp3play
#text = "Cześć co robisz?"
#text = urllib.quote_plus(text)
#print text
#url = u'http://translate.google.com/translate_tts?ie=UTF-8&tl=pl&q='+text
#request = urllib2.Request(url)
#request.add_header('User-agent', 'Mozilla/5.0') 
#opener = urllib2.build_opener()
#
#f = open("data.mp3", "wb")
#f.write(opener.open(request).read())
#f.close()

#import pyglet
#
#music = pyglet.resource.media('data.mp3')
#music.play()
#
#pyglet.app.run()
import time
import pygame
pygame.mixer.init()
sound = pygame.mixer.Sound('D:/PCAudioControl/data.mp3')
sound.play()
time.sleep (20)
