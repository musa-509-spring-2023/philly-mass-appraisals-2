function initMap() {
    const map = L.map('map-container').setView([39.98, -75.2], 12);
  
    const mapboxAccount = 'keelbn';
    const mapboxStyle = 'clg3y1y4q006401ppzs71inav';
    const mapboxToken = 'pk.eyJ1Ijoia2VlbGJuIiwiYSI6ImNqaWVseGZjZzA3emMzdnAxM296OTFjNG8ifQ.W2j9Y2mz4t6vGRyKJk_Nyw';
    L.tileLayer(`https://api.mapbox.com/styles/v1/${mapboxAccount}/${mapboxStyle}/tiles/256/{z}/{x}/{y}@2x?access_token=${mapboxToken}`, {
        maxZoom: 19,
        attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
    }).addTo(map);
    
  const colors = ["#f0bc1f", "#827345", "#9b76b8", "#482863"]
    //const tiles = downloadTiles();

	const url = "https://storage.googleapis.com/musa509s23_team02_public/tiles/properties/{z}/{x}/{y}.pbf"
  
  //put dependencies on filter chexkbox checked DOM, not created yet
  const vectorTileStyling = {
    property_tile_info: (properties, zoom) => { 
      var current_value = properties.current_assessed_value;
      var tax_year_value = properties.tax_year_assessed_value;
      var perc_change = ((current_value-tax_year_value)/tax_year_value)*100;
      var dollar_change = current_value-tax_year_value;
      if (current_value < 150000) {
        return ({ 
        fill: true,
        weight: 1,
        fillColor: colors[0],
        color: colors[0],
        fillOpacity: 0.8,
        opacity: 1,
        });
      } 
      if (current_value >= 150000 && current_value < 300000) {
        return ({ 
        fill: true,
        weight: 1,
        fillColor: colors[1],
        color: colors[1],
        fillOpacity: 0.8,
        opacity: 1,
        }); 
      }
      if (current_value >= 300000 && current_value < 430000) {
        return ({ 
        fill: true,
        weight: 1,
        fillColor: colors[2],
        color: colors[2],
        fillOpacity: 0.8,
        opacity: 1,
        }); 
      }
      if (current_value >= 430000) {
        return ({ 
        fill: true,
        weight: 1,
        fillColor: colors[3],
        color: colors[3],
        fillOpacity: 0.8,
        opacity: 1,
        }); 
      }
    }
  };


	var mapboxVectorTileOptions = {
		rendererFactory: L.canvas.tile,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://www.mapbox.com/about/maps/">MapBox</a>',
	  vectorTileLayerStyles: vectorTileStyling,
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