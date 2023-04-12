function initMap() {
    const map = L.map('map-container').setView([39.98, -75.2], 12);
  
    const mapboxAccount = 'keelbn';
    const mapboxStyle = 'clg3y1y4q006401ppzs71inav';
    const mapboxToken = 'pk.eyJ1Ijoia2VlbGJuIiwiYSI6ImNqaWVseGZjZzA3emMzdnAxM296OTFjNG8ifQ.W2j9Y2mz4t6vGRyKJk_Nyw';
    L.tileLayer(`https://api.mapbox.com/styles/v1/${mapboxAccount}/${mapboxStyle}/tiles/256/{z}/{x}/{y}@2x?access_token=${mapboxToken}`, {
        maxZoom: 19,
        attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
    }).addTo(map);
    
  
    //const tiles = downloadTiles();

	const url = "https://storage.googleapis.com/musa509s23_team02_public/tiles/properties/{z}/{x}/{y}.pbf"


	var mapboxVectorTileOptions = {
		rendererFactory: L.canvas.tile,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://www.mapbox.com/about/maps/">MapBox</a>',
	//	vectorTileLayerStyles: vectorTileStyling,
	//	token: 'pk.eyJ1IjoiaXZhbnNhbmNoZXoiLCJhIjoiY2l6ZTJmd3FnMDA0dzMzbzFtaW10cXh2MSJ9.VsWCS9-EAX4_4W1K-nXnsA'
	};

	var vectorGrid = L.vectorGrid.protobuf(url, mapboxVectorTileOptions)
	.addTo(map);
		
	
	map.vectorGrid = vectorGrid;
  
    return map;
  };

  export {
    initMap
  };