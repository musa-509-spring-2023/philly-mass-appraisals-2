import requests
import pathlib
import json
from google.cloud import storage
import functions_framework

#@functions_framework.http
#def extract_data(request):

storage_client = storage.Client()
bucket_name = "musa509spring2023_raw_data"
bucket = storage_client.bucket(bucket_name)

url = "https://phl.carto.com/api/v2/sql?filename=opa_properties_public&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+opa_properties_public"
resp = requests.get(url)
data = resp.json()

json_data = json.dumps(data)
blob = bucket.blob('phl_opa_properties/opa_rawdata.json')
blob.upload_from_string(json_data,content_type='application')

    #return 'OK'
