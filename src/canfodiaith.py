#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from urllib.parse import urlencode

import json

API_KEY='5a2b454d-0909-43dc-8699-877b0381f995'
API_LANG='cy'
API_URL='http://api.techiaith.org/langdetect/v1/?'


def get_from_api(text):
    
    params = {
        'text' : text.encode('utf-8'),
        'api_key' : API_KEY.encode('utf-8'),
        'lang' : API_LANG.encode('utf-8')
    }
    
    url = API_URL + urlencode(params)
    
    response = request.urlopen(url)
    response = json.loads(response.read().decode())

    if not response['success']:
        # Gwall gyda'r galwad API
        error_messages = '\n'.join(response['errors'])
        raise ValueError(error_messages)

    return response


def iaith_testun(text):

    result=get_from_api(text)    
    #
    # "result": {
    # 	"probabilities": {"cy": 0.9999919323188298},
    #   "lang": "cy"
    #}
    #
    return result['result']['lang']


if __name__ == "__main__":
    print(iaith_testun("Dwi'n byw yng Ngarndolbenmaen"))
    print(iaith_testun("And they all lived happily ever after"))
    print(iaith_testun("Je suis Charlie"))
    
    
