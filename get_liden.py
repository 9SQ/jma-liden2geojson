import sys, shutil
import json
import urllib.request
import xml.etree.ElementTree as et

argvs = sys.argv
argc = len(argvs)

if (argc > 1):
    datetime = argvs[1]
else:
    basetime_url = 'http://www.jma.go.jp/jp/highresorad/highresorad_tile/tile_basetime.xml'
    basetime_req = urllib.request.Request(basetime_url)
    with urllib.request.urlopen(basetime_req) as response:
        basetime_xml = response.read()
    basetime = et.fromstring(basetime_xml)
    datetime = basetime[0].text

data_url = 'http://www.jma.go.jp/jp/highresorad/highresorad_tile/LIDEN/'+datetime+'/'+datetime+'/none/data.xml'
data_req = urllib.request.Request(data_url)
with urllib.request.urlopen(data_req) as response:
    data_xml = response.read()
data = et.fromstring(data_xml)

features = []

for i,child in enumerate(data):
    if i is not 0:
        feature = {
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(child.attrib["lon"]),
                    float(child.attrib["lat"])
                ]
            },
            "type": "Feature",
            "properties": {
                "type": int(child.attrib["type"])
            }
        }
        features.append(feature)

featurecollection = {"type":"FeatureCollection","features":features}

f = open(datetime + ".json", "w")
f.write(json.dumps(featurecollection))
f.close()
shutil.copy(datetime + ".json", "recent.json")
print("save to " + datetime + ".json")