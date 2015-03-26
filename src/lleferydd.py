import urllib.request, urllib.parse
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

     
def llefaru(text):
    audio = get_speech_audio(text)
    print (text)
    play(audio)


def cwestiwn(text):
    llefaru(text)
    result=input()
    return result


def play(audio):
    aplay = Popen(['aplay', '-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    aplay.stdin.write(audio)
    aplay.communicate()

    
if __name__ == "__main__":

    llefaru('Mae hen wlad fy nhadau')
    ateb=cwestiwn("Wyt ti'n hoffi'r gan yna?")
    print (ateb)
    
