#!/usr/bin/python3

import requests

def main():
    neourl='https://api.nasa.gov/neo/rest/v1/feed?'
    startdate='start_date=2018-06-01'
    enddate='&end_date=END_DATE'
    mykey='&api_key=uJGCvEKptrXEqD9OG5xwTTfpsBup8eQzRka7Zkmo'

    neourl=neourl+startdate+mykey

    #neourlobj=urllib.request.urlopen(neourl)

    #neoread=neourlobj.read()
    #decodeneo=json.loads(neoread.decode('utf-8'))
    
    neojson=(requests.get(neourl)).json()
    print(neojson)

main()
