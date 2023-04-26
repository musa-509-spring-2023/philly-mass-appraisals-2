from urllib.request import urlopen
from google.cloud import storage
import dotenv 
dotenv.load_dotenv()

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\DELL\\Documents\\Github\\MUSA 509\\key\\musa509s23-team2-philly-cama-67593d6af962.json"


client = storage.Client()
bucket = client.bucket("musa509s23_team02_raw_data")

url = "https://phl.carto.com/api/v2/sql?format=geojson&skipfields=cartodb_id&q=SELECT%20*%20FROM%20assessments"
filename = 'assessments.csv'


response = urlopen(url)
blob = bucket.blob('opa_assessments/assessments.csv')
blob.upload_from_string(response.read(), content_type='application/csv')