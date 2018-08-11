import urllib2
import json
import config

def search(q):
    q = q.replace(' ', '+')
    url = "https://api.discogs.com/database/search?q=" + q + "&type=master&token=" + config.api_token
    json_obj = urllib2.urlopen(url)
    return json.load(json_obj)

while (True): 
    query = raw_input("Search album: ")
    if (query == "quit"):
        break
    try:
        data = search(query)["results"][0]
        artist, album= data["title"].split(' - ')
        year, label = data["year"], data["label"][0]
        print "\nTitle: " + album + '\n', "Artist: " + artist + '\n',"Year: " + year + '\n', "Label: " + label + '\n'
    except:
        print "\nNo results found.\n "



