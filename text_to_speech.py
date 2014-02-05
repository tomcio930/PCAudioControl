# -*- coding: utf-8 -*- 
import urllib2
import urllib
import pyglet
import time
from text_to_speech.player import Player
from text_to_speech.text_to_speech import TextToAudioConverter


text = "idź spać?"
converter = TextToAudioConverter()
converter.toMp3(text, "data.mp3")
p = Player()
p.play("data.mp3")

