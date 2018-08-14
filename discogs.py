import urllib2
import json
import config
import requests

def search(q):
    q = q.replace(' ', '+')
    url = "https://api.discogs.com/database/search?q=" + q + "&format_exact=Vinyl&type=release&token=" + config.api_token
    json_obj = urllib2.urlopen(url)
    return json.load(json_obj)

def suggested_prices(ID):
    url = "https://api.discogs.com/marketplace/price_suggestions/" + ID
    headers = {'Authorization': 'Discogs token=' + config.api_token}
    r = requests.get(url, headers=headers)
    return r.json()

def avg_prices(data, artist):
    total_prices = [0,0,0,0,0,0,0,0]
    total = 0
    for result in data["results"]:
        if artist != result["title"].split(' - ')[0]:
            break
        count = 0
        for value in suggested_prices(str(result["id"])).itervalues():
            total_prices[count] += (value["value"] if isinstance(value["value"], float) else 0)
            count += 1
        total += 1.0
    avg_prices = [i/total for i in total_prices]
    return avg_prices
        
if __name__ == '__main__':
    while (True): 
        query = raw_input("Search album: ")
        if (query == "quit"):
            break
        try:
            data = search(query)
            result0 = data["results"][0]
            artist, album= result0["title"].split(' - ')
            year, label = result0["year"], result0["label"][0]
            ID = str(result0["id"])
            print "\nTitle: " + album + '\n', "Artist: " + artist
            print "Year: " + year + '\n', "Label: " + label + '\n', "ID: " + ID + '\n'
            print "\nCalculating suggested prices...\n"
            try:
                prices = avg_prices(data, artist)   
                print "P: ", prices[5]
                print "F: ", prices[0]
                print "G: ", prices[1]
                print "G+: ", prices[2]
                print "VG: ", prices[6]
                print "VG+: ", prices[7]
                print "NM: ", prices[4]
                print "M: ", prices[3], '\n'
            except:
                print "You are making requests too quickly.\n"
        except:
            print "\nNo results found.\n "




