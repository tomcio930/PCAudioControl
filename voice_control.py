#!/usr/bin/env python
#Boa:PyApp:main
modules = {}


import ctypes

mixerSetControlDetails = (
    ctypes.windll.winmm.mixerSetControlDetails)
    
mixerGetControlDetails = (
    ctypes.windll.winmm.mixerGetControlDetailsA)

waveOutSetVolumeFun = (
    ctypes.windll.winmm.waveOutSetVolume)

result = waveOutSetVolumeFun(0, 0)
print 'result: '
# Some constants
MIXER_OBJECTF_MIXER = 0 # mmsystem.h
VOLUME_CONTROL_ID = 0     # Same on all machines?
SPEAKER_LINE_FADER_ID = 2# "Identifier <identifier> in OID value does not resolve to a positive integer"
MINIMUM_VOLUME = 0     # fader control (MSDN Library)
MAXIMUM_VOLUME = 65535 # fader control (MSDN Library)

class MIXERCONTROLDETAILS(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('cbStruct', ctypes.c_ulong),
                ('dwControlID', ctypes.c_ulong),
                ('cChannels', ctypes.c_ulong),
                ('cMultipleItems', ctypes.c_ulong),
                ('cbDetails', ctypes.c_ulong),
                ('paDetails', ctypes.POINTER(ctypes.c_ulong))]

def setVolume(volume):
    """Set the speaker volume on the 'Volume Control' mixer"""
    if not (MINIMUM_VOLUME <= volume <= MAXIMUM_VOLUME):
        raise ValueError, "Volume out of range"
    cd = MIXERCONTROLDETAILS(ctypes.sizeof(MIXERCONTROLDETAILS),
                             SPEAKER_LINE_FADER_ID,
                             1, 0,
                             ctypes.sizeof(ctypes.c_ulong),
                             ctypes.pointer(ctypes.c_ulong(volume)))
    ret = mixerSetControlDetails(VOLUME_CONTROL_ID,
                                 ctypes.byref(cd),
                                 MIXER_OBJECTF_MIXER)
    if ret != 0:
        print WindowsError, "Error %d while setting volume" % ret
        
    ret = mixerGetControlDetails(VOLUME_CONTROL_ID,
                                 ctypes.byref(cd),
                                 MIXER_OBJECTF_MIXER)
    if ret != 0:
        print WindowsError, "Error %d while setting volume" % ret
    else:
        print 'cbStruct', cd.cbStruct
        print 'dwControlID', cd.dwControlID
        print 'cChannels', cd.cChannels
        print 'cMultipleItems', cd.cMultipleItems
        print 'cbDetails', cd.cbDetails
        print 'paDetails', cd.paDetails.contents
    return


#setVolume(0) 



#from ctypes import *
#from struct import *
#
#winmm= windll.winmm
#print
#print 'waveOutGetNumDevs=',winmm.waveOutGetNumDevs()
#print 'mixerGetNumDevs', winmm.mixerGetNumDevs()
#
#wvcps= ' '*52
#print 'res:', winmm.waveOutGetDevCapsA(0,wvcps,len(wvcps))
#
#res = unpack('IIL32cLI', wvcps)
#print res
#wMid=res[0]
#wPid=res[1]
#vDriverVersion=res[2]
#szPname=''.join(res[3:35])
#dwFormats=res[35]
#wChannels=res[36]
#print 'wMid=',wMid
#print 'wPid=',wPid
#print 'vDriverVersion=',vDriverVersion
#print 'szPname=',szPname
#print 'dwFormats=',dwFormats
#print 'wChannels=',wChannels
#
#vol=c_ulong()
#print 'res', winmm.waveOutGetVolume(0, byref(vol))
#
#print 'l:', vol.value & 0xffff, 'r:',vol.value >> 16 # left, right