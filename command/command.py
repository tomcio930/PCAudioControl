#-*- coding: utf-8 -*-
'''
Created on 27-01-2014

@author: Tomek
'''

import speech
from subprocess import call
class Command():
    def __init__(self):
        self.supportedCommands = {u'wyłącz':'shutdown', 'anuluj':'cancel_shutdown', 'youtube':'youtube'}
     
    def cancel_shutdown(self):
        call(["shutdown", "-a"])
        speech.say("Cancel shutdown.")
     
    def shutdown(self):
        speech.say("Goodbye Tomekk.")
        call(["shutdown", "-s", "-t", "1200"])
         
    def chrome(self):
        call(["chrome.exe"])
        speech.say("Chrome is opening.")
         
    def youtube(self):
        call(["chrome.exe", "http://www.youtube.com/watch?v=iJKQOw5JikQ&list=PLQ3Z41XSDThouMRoUz2hxN7Nr2dmRzSL6"])
        speech.say("Youtube is opening.")
        
    def getSupportedCommands(self):
        return self.supportedCommands