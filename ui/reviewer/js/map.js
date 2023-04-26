const colors = ["#f0bc1f", "#827345", "#9b76b8", "#482863"]
const checkboxes = document.querySelectorAll('.filter-checkbox');

function styleBy(field){
    if (field < 150000) {
    return ({ 
    fill: true,
    weight: 1,
    fillColor: colors[0],
    color: colors[0],
    fillOpacity: 0.8,
    opacity: 1,
    });
  } else if (field  >= 150000 && field < 300000) {
    return ({ 
    fill: true,
    weight: 1,
    fillColor: colors[1],
    color: colors[1],
    fillOpacity: 0.8,
    opacity: 1,
    }); 
  } else if (field  >= 300000 && field  < 430000) {
    return ({ 
    fill: true,
    weight: 1,
    fillColor: colors[2],
    color: colors[2],
    fillOpacity: 0.8,
    opacity: 1,
    }); 
  } else if (field  >= 430000) {
    return ({ 
    fill: true,
    weight: 1,
    fillColor: colors[3],
    color: colors[3],
    fillOpacity: 0.8,
    opacity: 1,
    }); 
  } else {
    return ({ 
      fill: true,
      weight: 1,
      fillColor: colors[0],
      color: colors[0],
      fillOpacity: 0.8,
      opacity: 1,
      });
  }
};

var display = 0;

for (const checkbox of checkboxes){
  checkbox.addEventListener('change', (evt) => {
      if (evt.target.checked){
          console.log('you clicked on the checkbox ' + checkbox.value);
          if (checkbox.value == 1){
            display = 1;
          } else  if (checkbox.value == 2){
            display = 2;
          } else if (checkbox.value == 3){
            display = 3;
          } else {
            display = 4
          }
      } else {
          console.log('you unclicked the checkbox ' + checkbox.value);
      }
  });
}
      
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

  var vectorTileStyling = {
        
    property_tile_info: (properties, zoom) => { 
        
      var current_value = properties.current_assessed_value;
      var tax_year_value = properties.tax_year_assessed_value;
      var perc_change = ((current_value-tax_year_value)/tax_year_value)*100;
      var dollar_change = current_value-tax_year_value;
      if (display==1){
        return styleBy(current_value);
      } else if (display==2){
        return styleBy(tax_year_value);
      } else if (display==3) {
        return styleBy(perc_change);
      } else if (display==4) {
        return styleBy(dollar_change);
      } else {
        return ({ 
          fill: true,
          weight: 1,
          fillColor: colors[0],
          color: colors[0],
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