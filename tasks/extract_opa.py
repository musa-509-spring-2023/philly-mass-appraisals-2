from urllib.request import urlopen
import pathlib
from google.cloud import storage

# RAW_DATA_DIR = pathlib.Path(__file__).parent/ 'raw_data'
client = storage.Client()
bucket = client.get_bucket("musa509s23_team2_raw_data")

url = "https://phl.carto.com/api/v2/sql?filename=opa_properties_public&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+opa_properties_public"
filename = 'opa.geojson'

response = urlopen(url)
# with open(RAW_DATA_DIR / filename, 'wb') as f:
#     while True:
#         chunck = response.read(1024 * 1024)
#         if not chunck:
#             break
#         f.write(chunck)

blob = bucket.blob('phl/opa.geojson')
blob.upload_from_string(response, content_type = 'application/geojson')