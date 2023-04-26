import json
from urllib.request import urlopen
import io
from google.cloud import storage
import dotenv
dotenv.load_dotenv()

# RAW_DATA_DIR = pathlib.Path(__file__).parent/ 'raw_data'
# PROCESSED_DATA_DIR = pathlib.Path(__file__).parent / 'processed_data'
client = storage.Client()
bucket = client.bucket("musa509s23_team02_prepared_data")

blob = bucket.blob("opa_properties/opa.geojson")
content = blob.download_as_string()

# with open(RAW_DATA_DIR/'opa.geojson', 'rU', encoding='utf-8') as f:

data = json.loads(content)

processed_blob = bucket.blob('opa_assessments/opa_assessments.jsonl')

jsonl_data = []
for feature in data['features']:
    row = feature['properties']
    row['geog'] = json.dumps(feature['geometry'])
    jsonl_data.append(json.dumps(row))

processed_blob.upload_from_string('\n'.join(jsonl_data), content_type = 'application/jsonl')

#with open(PROCESSED_DATA_DIR / 'opa_propeorties.jsonl', 'w') as f:
  #for feature in data['features']:
  #    row = feature['properties']
  #    row['geog'] = json.dumps(feature['geometry'])
  #    f.write(json.dumps(row) + '\n')
  #
  #  processed_blob.upload_from_file(




import csv
import io
import json
from google.cloud import storage
import functions_framework

@functions_framework.http
def prepare_opa_assessments(request):
    client = storage.Client()
    raw_bucket = client.bucket('mjumbewu_musa_509_raw_data')
    processed_bucket = client.bucket('mjumbewu_musa_509_processed_data')

    raw_blob = raw_bucket.blob('census/census_population_2020.json')
    content = raw_blob.download_as_string()
    data = json.loads(content)
    data[0] = ['name', 'geoid', 'population', 'state', 'county', 'tract', 'block_group']

    processed_blob = processed_bucket.blob('census_population_2020/data.csv')
    outfile = io.StringIO()
    writer = csv.writer(outfile)
    writer.writerows(data)
    processed_blob.upload_from_string(outfile.getvalue(), content_type='text/csv')

    return 'OK'