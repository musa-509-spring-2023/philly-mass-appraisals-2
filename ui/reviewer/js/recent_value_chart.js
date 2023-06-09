async function showRecentValueChart() {
  let data = await fetchChartData();
  console.log(data);

  // Get the max tax year from the data.
  const latestTaxYear = Math.max(...data.map(row => row.tax_year));

  // Filter the data just for the latest tax year.
  data = data.filter(row => row.tax_year == latestTaxYear);

  renderChart(data);
}

async function fetchChartData() {
  const response = await fetch('https://storage.googleapis.com/musa509s23_team01_public/configs/tax_year_assessment_bins.json');
  const data = await response.json();
  return data;
}

function renderChart(data) {
  // Calculate the total number of properties in the data.
  let totalProperties = data.map(row => row.property_count).reduce((a, b) => a + b, 0);
  console.log('totalProperties', totalProperties);

  // Get the 97.5th percentile price.
  const percentile = 0.975;
  const percentileCutoff = Math.floor(totalProperties * percentile);
  console.log('percentileCutoff', percentileCutoff);

  let priceCutoff = 0;
  let cumulativePropertyCount = 0;
  for (const row of data) {
    cumulativePropertyCount += row.property_count;
    if (cumulativePropertyCount >= percentileCutoff) {
      priceCutoff = row.upper_bound;
      break;
    }
  }
  console.log('priceCutoff', priceCutoff);

  // Build the X and Y arrays for the chart.
  let Y = [];
  let X = [];
  let countBeyondLimit = 0;
  for (const row of data) {
    if (row.upper_bound < priceCutoff) {
      Y.push(row.property_count);
      X.push(row.upper_bound);
    } else {
      countBeyondLimit += row.property_count;
    }
  }
  Y.push(countBeyondLimit);
  X.push(priceCutoff);

  // Render the chart.
  var options = {
    series: [{
      name: 'Number of Properties',
      data: Y,
    }],
    chart: {
      height: 250,
      type: 'area'
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 1.5,
    },
    xaxis: {
      type: 'numeric',
      categories: X,
      title: {
        text: 'Assessment Value',
      },
      labels: {
        formatter: function (val) {
          return '$' + (
            val < 1000 ?    val.toFixed(0) :
            val < 1000000 ? (val / 1000).toFixed(0) + 'k' :
                            (val / 1000000).toFixed(1) + 'M'
          ) + (val === priceCutoff ? '+' : '');
        }
      },
    },
    yaxis: {
      title: {
        text: 'Number of Properties',
      }
    },
  };

  var chart = new ApexCharts(document.querySelector(".recent-graph-continer"), options);
  chart.render();
  return chart;
}

export {
  showRecentValueChart,
}