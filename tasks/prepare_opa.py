import json
import pathlib

# RAW_DATA_DIR = pathlib.Path(__file__).parent/ 'raw_data'
# PROCESSED_DATA_DIR = pathlib.Path(__file__).parent / 'processed_data'

with open(RAW_DATA_DIR/'opa.geojson', 'rU', encoding='utf-8') as f:
    data = json.load(f)

with open(PROCESSED_DATA_DIR / 'opa_propeorties.jsonl', 'w') as f:
    for feature in data['features']:
        row = feature['properties']
        row['geog'] = json.dumps(feature['geometry'])
        f.write(json.dumps(row) + '\n')