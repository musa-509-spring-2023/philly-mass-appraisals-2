import { initMap } from './map.js';
import { showRecentValueChart } from './recent_value_chart.js';

console.log("main");

const map = initMap();
const recentValueChart = showRecentValueChart();

window.mapview = map;
window.recentValueChart = recentValueChart;
