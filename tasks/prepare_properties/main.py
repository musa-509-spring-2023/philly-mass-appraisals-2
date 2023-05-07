import json
from google.cloud import storage
import functions_framework
import dotenv
dotenv.load_dotenv()


@functions_framework.http
def prepare_properties(request):
    client = storage.Client()
    bucket = client.bucket("musa509s23_team02_raw_data")

    blob = bucket.blob("opa_properties/opa.geojson")
    content = blob.download_as_string()

    data = json.loads(content)

    processed_blob = bucket.blob('opa_properties/opa_processed.jsonl')

    jsonl_data = []
    for feature in data['features']:
        row = feature['properties']
        row['geog'] = json.dumps(feature['geometry'])
        jsonl_data.append(json.dumps(row))

    processed_blob.upload_from_string('\n'.join(jsonl_data), content_type='application/jsonl')

    return 'OK'
