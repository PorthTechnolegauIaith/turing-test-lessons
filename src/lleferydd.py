import urllib, urllib.parse
import os
import random, string
from subprocess import Popen, PIPE, STDOUT



API_KEY = "65f7ef45-fe56-4aac-a787-9a64fa065af4"
API_LANG = 'cy'
API_URL = "http://api.techiaith.org/festival/v1/?"


def get_random_filename(length=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))
   

def get_speech_audio(text):

    filename = '%s.mp3' % get_random_filename()
    
    with open(filename , 'wb') as f:
        params = {
        'api_key': API_KEY,
        'lang': API_LANG,
        'text': text
    }
        
    url = API_URL + urllib.parse.urlencode(params)    
    with open (filename, 'wb') as f:
        f.write(urllib.request.urlopen(url).read())

    return filename


     
def llefaru(text):

    v="30"
    filename = get_speech_audio(text)

    pplay = Popen(['mpg321', '-R', '-F', 'anyword'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    if (os.path.isfile(filename)):
        bfile = filename.encode('utf-8')
        svol = str(v)
        bvol = svol.encode('utf-8')
        pplay.stdin.write(b'GAIN ' + bvol + b'\n')
        pplay.stdin.write(b'LOAD ' + bfile + b'\n')
        playon = 1
        while playon == 1:
            pleng = pplay.stdout.readline()
            if b'@P' in pleng: playon = 0
            else: playon = 1

    pplay.stdin.write(b'QUIT')
        
    
