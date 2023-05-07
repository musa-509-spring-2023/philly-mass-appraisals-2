import json
from google.cloud import storage
import dotenv
dotenv.load_dotenv()
import csv
import os
import io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\DELL\\Documents\\Github\\MUSA 509\\key\\musa509s23-team2-philly-cama-67593d6af962.json"


client = storage.Client()
raw_bucket =  client.bucket("musa509s23_team02_raw_data")
processed_bucket =client.bucket("musa509s23_team02_prepared_data")
raw_blob = raw_bucket.blob("opa_assessments/assessments.csv")
processed_blob = processed_bucket.blob('opa_assessments/assessments.csv')
content = raw_blob.download_as_string()
data = json.loads(content)
outfile = io.StringIO()
writer = csv.writer(outfile)
writer.writerows(data)
processed_blob.upload_from_string(outfile.getvalue(), content_type = "text/csv")



