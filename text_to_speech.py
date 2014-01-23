# -*- coding: utf-8 -*- 
import urllib2
import urllib
text = "Good morning. What i can do for you?"
text = "Bye Bye. See you tomorrow."
text = urllib.quote_plus(text)
print text
url = u'http://translate.google.com/translate_tts?ie=UTF-8&tl=en-us&q='+text
request = urllib2.Request(url)
request.add_header('User-agent', 'Mozilla/5.0') 
opener = urllib2.build_opener()

f = open("data.mp3", "wb")
f.write(opener.open(request).read())
f.close()