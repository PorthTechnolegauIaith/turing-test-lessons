import urllib.request, urllib.parse
import os
import random, string
from subprocess import Popen, PIPE, STDOUT

API_KEY = "65f7ef45-fe56-4aac-a787-9a64fa065af4"
API_LANG = 'cy'
API_URL = "http://api.techiaith.org/festival/v1/?"
   
def get_speech_audio(text):
    
    params = {
        'api_key': API_KEY,
        'lang': API_LANG,
        'text': text,
        'format': 'wav'
    }
        
    url = API_URL + urllib.parse.urlencode(params)    
    return urllib.request.urlopen(url).read()

    return filename
     
def llefaru(text):
    audio = get_speech_audio(text)

    aplay = Popen(['aplay', '-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    aplay.stdin.write(audio)
    aplay.communicate()

if __name__ == "__main__":
    llefaru('helo')
