import json
from google.cloud import storage
import dotenv
dotenv.load_dotenv()
import csv
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\DELL\\Documents\\Github\\MUSA 509\\key\\musa509s23-team2-philly-cama-67593d6af962.json"


client = storage.Client()
bucket = client.bucket("musa509s23_team02_raw_data")
raw_bucket =  client.bucket("musa509s23_team02_raw_data")
processed_bucket =client.bucket("musa509s23_team02_prepared_data")
raw_blob = raw_bucket.blob("opa_assessments/assessments.csv")
processed_blob = processed_bucket.blob('opa_assessments/assessments.jsonl')

content = raw_blob.download_as_string()
data = csv.DictReader(content.decode('utf-8').splitlines())
jsonl_data = [json.dumps(row) for row in data]

processed_blob.upload_from_string('\n'.join(jsonl_data), content_type = 'application/jsonl')


