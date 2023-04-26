import csv
import io
import json
from google.cloud import storage
import functions_framework


@functions_framework.http
def prepare_assessments(request):
    client = storage.Client()
    raw_bucket =  client.bucket("musa509s23_team02_prepared_data")
    processed_bucket = raw_bucket.blob('opa_assessments/assessments.jsonl')
    raw_blob = raw_bucket.blob("opa_assessments/assessments.csv")
    csv_data = raw_blob.download_as_string().decode('utf-8')
    # Convert CSV data to JSONL format
    jsonl_data = []
    for row in csv.DictReader(csv_data.splitlines()):
      jsonl_data.append(json.dumps(row))

    processed_blob = processed_bucket.upload_from_string('\n'.join(jsonl_data), content_type = 'application/jsonl')
    
    return 'OK'