'''
Created on 05-02-2014

@author: Tomek
'''
import pyglet, time

class Player(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    def play(self, audio_path):
        sound = pyglet.media.load(audio_path)
        duration = sound._get_duration()
        sound.play()
        time.sleep(duration)
        