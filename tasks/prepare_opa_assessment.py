import json
from google.cloud import storage
import dotenv
dotenv.load_dotenv()

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\DELL\\Documents\\Github\\MUSA 509\\key\\musa509s23-team2-philly-cama-67593d6af962.json"
# RAW_DATA_DIR = pathlib.Path(__file__).parent/ 'raw_data'
# PROCESSED_DATA_DIR = pathlib.Path(__file__).parent / 'processed_data'
client = storage.Client()
bucket = client.bucket("musa509s23_team02_raw_data")

blob = bucket.blob("opa_assessments/assessments.geojson")
content = blob.download_as_string()

# with open(RAW_DATA_DIR/'opa.geojson', 'rU', encoding='utf-8') as f:

data = json.loads(content)
processed_blob = bucket.blob('opa_assessments/data.jsonl')

jsonl_data = []
for feature in data['features']:
    row = feature['properties']
    #row['geog'] = json.dumps(feature['geometry'])
    jsonl_data.append(json.dumps(row))

processed_blob.upload_from_string('\n'.join(jsonl_data), content_type = 'application/jsonl')

#with open(PROCESSED_DATA_DIR / 'opa_propeorties.jsonl', 'w') as f:
  #for feature in data['features']:
  #    row = feature['properties']
  #    row['geog'] = json.dumps(feature['geometry'])
  #    f.write(json.dumps(row) + '\n')
  #
  #  processed_blob.upload_from_file(
