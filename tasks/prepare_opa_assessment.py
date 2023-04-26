import json
from google.cloud import storage
import dotenv
dotenv.load_dotenv()
import csv
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\DELL\\Documents\\Github\\MUSA 509\\key\\musa509s23-team2-philly-cama-67593d6af962.json"


client = storage.Client()
bucket = client.bucket("musa509s23_team02_prepared_data")

blob = bucket.blob("opa_assessments/assessments.csv")
# Download the CSV file as a string
csv_data = blob.download_as_string().decode('utf-8')

processed_blob = bucket.blob('opa_assessments/assessments.jsonl')
# Convert CSV data to JSONL format
jsonl_data = []
for row in csv.DictReader(csv_data.splitlines()):
    jsonl_data.append(json.dumps(row))

processed_blob.upload_from_string('\n'.join(jsonl_data), content_type = 'application/jsonl')


