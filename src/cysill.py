#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from collections import OrderedDict
from urllib import request
from urllib.parse import urlencode

import json

API_KEY = "ea438988-b88a-4b95-97b8-bf055fa64631"

# Api lang parameter can be either 'cy' or 'en'
# Gellir defnyddio 'cy' neu 'en' ar gyfer iaith yr API
API_LANG = 'cy'

API_URL = "http://api.techiaith.org/cysill/v1/?"


#class Colour:
#    RED = '\033[91m'
#    BLUE = '\033[94m'
#    GREEN = '\033[92m'
#    END = '\033[0m'


# checker ar gyfer gwirio'r sillafu
def get_errors(llinell):
    params = {
        'api_key': API_KEY,
        'lang': API_LANG,
        'text': llinell
    }
    url = API_URL + urlencode(params)
    
    response = request.urlopen(url)
    response = json.loads(response.read().decode())
    if not response['success']:
        # Gwall gyda'r galwad API
        error_messages = '\n'.join(response['errors'])
        raise ValueError(error_messages)
    
    return response['result']

GEIRIADU_WEDI_ANWYBYDDU = []

def gwirio_testun(testun):

    with open('geiriadur.txt', 'r') as g:
        geiriadur_personol = set(l.strip() for l in g.read().split('\n'))

    print ("Yn gwirio.... %s" % testun)
    
    errors = get_errors(testun)

    if not len(errors):
        return testun, 0
    else:
        print ("Roedd %s wall yn eich destun " % len(errors))
    
    nifer_gwiriadau = 0

    for error in errors:
        
        gair_camsillafu = testun[error['start']:error['start'] + error['length']]
        if gair_camsillafu in GEIRIADU_WEDI_ANWYBYDDU or gair_camsillafu.lower() in GEIRIADU_WEDI_ANWYBYDDU:
            continue

        if (gair_camsillafu in geiriadur_personol) or (gair_camsillafu.lower() in geiriadur_personol):
            print ("Rwyf wedi dysgu gen ti bod '$s' yn gywir " % gair_camsillafu)
            continue

        print((("\nGWALL %s:  " % ("SILLAFU" if error['isSpelling'] else 'GRAMADEG')) +
            #testun[0:error['start']] + Colour.RED + gair_camsillafu + Colour.END +
            testun[0:error['start']] + gair_camsillafu +
            testun[error['start']+error['length']:]))

        nifer_awgrymiadau = len(error['suggestions'])
        awgrym = None

        print("%s.\n\nDewisiwch opsiwn canlynol:\n--------------------------" % error['message'])

        #opsiynau = (('a', 'Anwybyddu'), ('y', "Ychwanegu '%s%s%s' i'r geiriadur" % (Colour.RED, gair_camsillafu, Colour.END)), ('m', 'Mewnbynnu cywiriad eich hun'))
        opsiynau = (('a', 'Anwybyddu'), ('y', "Ychwanegu '%s' i'r geiriadur" % gair_camsillafu), ('m', 'Mewnbynnu cywiriad eich hun'))

        if nifer_awgrymiadau:
            opsiynau += tuple([(str(i+1), "Cywiro i '%s'" % sugg) for i, sugg in enumerate(error['suggestions'])])
        
        opsiynau_dict = OrderedDict(opsiynau)
        
        print('\n'.join("[{}] {}".format(k,v) for k,v in opsiynau_dict.items()))
        
        ans = -1
        while (not opsiynau_dict.get(ans)):
            ans = input("Dewisiwch opsiwn (%s): " % ', '.join(opsiynau_dict.keys())).lower()

        print (ans)
        
        if ans == 'a':
            # anwybyddu
            GEIRIADU_WEDI_ANWYBYDDU.append(gair_camsillafu)
            continue
        elif ans == 'y':
            # ychwanegu i'r geiriadur
            geiriadur_personol.add(gair_camsillafu)

            with open('geiriadur.txt', 'w') as g:
                g.write('\n'.join(sorted(geiriadur_personol)))

        elif ans == 'm':
            # mewnbynnu testun eich hun
            #awgrym = input("Ysgrifennwch testun i cywiro '%s%s%s': " % (Colour.RED, gair_camsillafu, Colour.END)).strip()
            awgrym = input("Ysgrifennwch testun i cywiro '%s': " %  gair_camsillafu).strip()
        else:
            try:
                awgrym = error['suggestions'][int(ans)-1]
            except ValueError:
                continue

        if awgrym is not None:
            nifer_gwiriadau += 1
            testun = testun[0:error['start']] + awgrym + testun[error['start']+error['length']:]
            # diweddaru start positions pob 'error' arral
            for pob_err in errors[errors.index(error)+1:]:
                pob_err['start'] += len(awgrym) - len(gair_camsillafu)
        
    return testun, nifer_gwiriadau
