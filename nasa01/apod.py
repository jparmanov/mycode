#!/usr/bin/python3

import urllib.request
import json
import webbrowser

apodurl='https://api.nasa.gov/planetary/apod?'
mykey='api_key=uJGCvEKptrXEqD9OG5xwTTfpsBup8eQzRka7Zkmo'

apodurlobj=urllib.request.urlopen(apodurl+mykey)
apodread=apodurlobj.read()

decodeapod=json.loads(apodread.decode('utf-8'))

print('\n\nConverted python data')
print (decodeapod)

input('\/Press Enter to open NASA Picture of the Dat in Firefox')
webbrowser.open(decodeapod['url'])
