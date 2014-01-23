import sys
import pyaudio
import speex
import numpy as np  # just for doing a standard deviation for audio level checks
import urllib2
import json
from subprocess import call
import speech

class VoiceRecognizer():
    def __init__(self, chunk=320, FORMAT=pyaudio.paInt16, CHANNELS=1, RATE=16000):
        self.isListening = True
        self.p = pyaudio.PyAudio()
        self.chunk = chunk
        # Start the stream to record the audio
        self.stream = self.p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        output = True,
                        frames_per_buffer = chunk)
        self.e = speex.Encoder()
        self.e.initialize(speex.SPEEX_MODEID_WB)
        self.d = speex.Decoder()
        self.d.initialize(speex.SPEEX_MODEID_WB)
    
    def __readStream(self, data):
        spxdata = self.e.encode(data) # encode using the speex dll
        return chr(len(spxdata))+spxdata
    
    def __isSilent(self, data, threshold=200):
        audioLevel = self.__getAudioLevel(data)
        if(audioLevel < threshold): # too quiet
            return True
        else:
            return False
        
    def __getAudioLevel(self, data):
        a=np.frombuffer(data,np.int16) # convert to numpy array to check for silence or audio
        return np.std(a)
    
    def __sendRequest(self, data):
        # see http://sebastian.germes.in/blog/2011/09/googles-speech-api/ for a good description of the url
        url = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&pfilter=1&client=chromium&lang=pl&maxresults=4'
        header = {'Content-Type' : 'audio/x-speex-with-header-byte; rate=16000'}
        req = urllib2.Request(url, data, header)
        return urllib2.urlopen(req)
    
    def record(self, threshold=200, silentFramesThreshold=40):
        spxlist=[]  # list of the encoded speex packets/frames
        loop_counter = 0
        silentFrames = 0
        listening = True
        while listening:
            loop_counter += 1
            data = self.stream.read(self.chunk) # grab 320 samples from the microphone
            spxlist.append(self.__readStream(data))
            if self.__isSilent(data, threshold):
                silentFrames += 1
            else:
                silentFrames = 0
            if silentFrames >= silentFramesThreshold:
                listening = False
            #print '(%d%% quiet)'%(silentFrames*100/silentFramesThreshold)
        if(loop_counter == silentFrames):
            return False
        else:
            return ''.join(spxlist) # make a string of all the header-ized speex packets
        
    def recognize(self, audioData):
        print 'Sending to Google.'
        response = voiceRecognizer.__sendRequest(audioData)
        print 'Google says:'
        data = response.read()
        print data
        jsdata = json.loads(data)
        hypotheses = jsdata["hypotheses"]
        if(hypotheses.__len__() == 0):
            print "Audio was not recognized. Please repeat."
            return ""
        else:
            return jsdata["hypotheses"][0]["utterance"]

class Command():
    def __init__(self):
        pass
     
    def cancel_shutdown(self):
        call(["shutdown", "-a"])
     
    def shutdown(self):
        call(["shutdown", "-s", "-t", "1200"])
         
    def chrome(self):
        call(["chrome.exe"])
         
    def youtube(self):
        call(["chrome.exe", "youtube.pl"]) 
         
cmd = Command()
#cmd.youtube()
#voiceRecognizer = VoiceRecognizer()
speech.say("Youtube is starting.")
while False:
    data = voiceRecognizer.record()
    if(data == False):
        print "Still listening..."
    else:
        recognizedAudio = voiceRecognizer.recognize(data)
        print "Text: "+recognizedAudio
        