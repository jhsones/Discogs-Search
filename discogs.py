import urllib2
import json
import config
import requests

def search(q):
    q = q.replace(' ', '+')
    url = "https://api.discogs.com/database/search?q=" + q + "&format_exact=Vinyl&type=release&token=" + config.api_token
    json_obj = urllib2.urlopen(url)
    return json.load(json_obj)

def suggested_price(ID):
    url = "https://api.discogs.com/marketplace/price_suggestions/" + ID
    headers = {'Authorization': 'Discogs token=' + config.api_token}
    r = requests.get(url, headers=headers)
    return r.json()

while (True): 
    query = raw_input("Search album: ")
    if (query == "quit"):
        break
    try:
        data = search(query)["results"][0]
        artist, album= data["title"].split(' - ')
        year, label = data["year"], data["label"][0]
        ID = str(data["id"])
        price = suggested_price(ID)
        print "\nTitle: " + album + '\n', "Artist: " + artist + '\n',"Year: " + year + '\n', "Label: " + label + '\n', "ID: " + ID + '\n'
        print json.dumps(price, indent=4, sort_keys=True)
    except:
        print "\nNo results found.\n "



