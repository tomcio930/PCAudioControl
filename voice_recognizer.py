#-*- coding: utf-8 -*-
import pyaudio
import speex
import numpy as np  # just for doing a standard deviation for audio level checks
import urllib2
import json
import speech
from subprocess import call
from command.command import Command
from voice_recognizer.voice_recognizer import VoiceRecognizer

         
cmd = Command()
voiceRecognizer = VoiceRecognizer()

while True:
    recognized_text = voiceRecognizer.live_recognize()
    print recognized_text
    if(recognized_text in cmd.supported_commands.keys()):
        getattr(cmd, cmd.supported_commands[recognized_text])() #call cmd method
        
        