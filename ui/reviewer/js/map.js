function initMap() {
    const map = L.map('map').setView([39.98, -75.2], 11.25);
  
    const mapboxAccount = 'keelbn';
    const mapboxStyle = 'clg3y1y4q006401ppzs71inav';
    const mapboxToken = 'pk.eyJ1Ijoia2VlbGJuIiwiYSI6ImNqaWVseGZjZzA3emMzdnAxM296OTFjNG8ifQ.W2j9Y2mz4t6vGRyKJk_Nyw';
    L.tileLayer(`https://api.mapbox.com/styles/v1/${mapboxAccount}/${mapboxStyle}/tiles/256/{z}/{x}/{y}@2x?access_token=${mapboxToken}`, {
        maxZoom: 19,
        attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
    }).addTo(map);
  
    // map.treeLayer = L.geoJSON(null, {
    //   pointToLayer: (feature, latlng) => L.circleMarker(latlng),
    //   style: {
    //     fillColor: '#83bf15',
    //     fillOpacity: 0.3,
    //     stroke: false,
    //   },
    // }).addTo(map);
  
    map.positionLayer = L.geoJSON(null).addTo(map);
  
    return map;
  };

  export {
    initMap
  };