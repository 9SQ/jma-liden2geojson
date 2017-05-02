//対地放電と雲放電のスタイル
var styles = {
    '0': [new ol.style.Style({
        image: new ol.style.Icon( /** @type {olx.style.IconOptions} */ ({
            scale: 0.5,
            src: 'images/0.png'
        }))
    })],
    '1': [new ol.style.Style({
        image: new ol.style.Icon( /** @type {olx.style.IconOptions} */ ({
            scale: 0.5,
            src: 'images/1.png'
        }))
    })],
};

//GeoJSONのproperties->typeに応じてstyleを反映
var styleFunction = function(feature, resolution) {
    return styles[feature.get('type')];
};

var liden_layer = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'recent.json',
        format: new ol.format.GeoJSON()
    }),
    style: styleFunction,
    minResolution: 20,
    maxResolution: 10000
});

var map = new ol.Map({
    target: 'map',
    renderer: 'canvas',
    layers: [
        //マップのレイヤー
        new ol.layer.Tile({
            source: new ol.source.OSM
        }),
        //ポイント
        liden_layer
    ],
    view: new ol.View({
        //中心座標
        center: ol.proj.transform([139.75, 35.68], 'EPSG:4326', 'EPSG:3857'),
        zoom: 7,
        minResolution: 20
    })
});