jma-liden2geojson
======

Lightning Information from JMA(Japan Meteorological Agency) convert to GeoJSON

## Description

Getting lightning information from [JMA High-resolution Precipitation Nowcasts](http://www.jma.go.jp/en/highresorad/) and convert to GeoJSON.

[気象庁 高解像度降水ナウキャスト](http://www.jma.go.jp/jp/highresorad/)の**雷情報**から、雲放電、対地放電の座標ををGeoJSONで出力します。

### Files

* get_liden.py - code (python3)
* recent.json - sample GeoJSON (May 1, 2017, 13:30 JST)
* viewer.html - sample web viewer (using OpenLayers 4.1.0)
* js/maprenderer.js - same as above
* images/0.png - cloud discharge icon
* images/1.png - ground discharge icon

## How to use

get recent information.
```sh
python get_liden.py
```

get information of specified date and time.
```sh
python get_liden.py 201705010430
```

## GeoJSON format
```json
{
	"type": "FeatureCollection",
	"features": [{
		"geometry": {
			"type": "Point",
			"coordinates": [lon, lat]
		},
		"type": "Feature",
		"properties": {
			"type": 0(cloud discharge) or 1(ground discharge)
		}
	}]
}
```