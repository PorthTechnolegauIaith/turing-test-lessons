#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from urllib.parse import urlencode

import json

API_KEY='8fda034e-3887-4877-82d5-b20cfdb4537f'
API_LANG='cy'
API_URL='http://api.techiaith.org/pos/v1/?'


def get_from_api(text):
    
    params = {
        'text' : text.encode('utf-8'),
        'api_key' : API_KEY.encode('utf-8'),
        'lang' : API_LANG.encode('utf-8')
    }
    
    url = API_URL + urlencode(params)

    print (url)
    
    response = request.urlopen(url)
    response = json.loads(response.read().decode())
    if not response['success']:
        # Gwall gyda'r galwad API
        error_messages = '\n'.join(response['errors'])
        raise ValueError(error_messages)
    
    return response['result']

def tag_text(text):
    
    tagged_text = get_from_api(text)
    for tagged_word in tagged_text.split(" "):
        word, pos, mutation = tagged_word.split("/")
        if mutation == "-":
            mutation = None
        elif mutation is "?":
            mutation = "Unknown"
        print("WORD: {}\nPOS: {}\nMUTATION: {}\n-----------".format(word, pos, mutation))


if __name__ == "__main__":
    tag_text("Dwi'n byw yng Ngarndolbenmaen")
    
