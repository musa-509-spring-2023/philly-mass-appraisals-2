import { initMap } from './map.js';

console.log("main");

let app = {
  currentTree: null,
  notes: null,
};

const loadOverlayEl = document.getElementById('load-overlay');
const map = initMap();

window.app = app;