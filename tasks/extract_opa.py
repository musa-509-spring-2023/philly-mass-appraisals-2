from urllib.request import urlopen
from google.cloud import storage
import dotenv 
dotenv.load_dotenv()
import functions_framework

# import os
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/huyh/Documents/Penn/Spring 2023/Cloud Computing/class-project/philly-mass-appraisals-2/key/musa509s23-team2-philly-cama-67593d6af962.json"

# RAW_DATA_DIR = pathlib.Path(__file__).parent/ 'raw_data'

@functions_framework.http(request):
def extract_opa
client = storage.Client()
bucket = client.bucket("musa509s23_team02_raw_data")

url = "https://phl.carto.com/api/v2/sql?filename=opa_properties_public&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+opa_properties_public"
filename = 'opa.geojson'

response = urlopen(url)
# with open(RAW_DATA_DIR / filename, 'wb') as f:
#     while True:
#         chunck = response.read(1024 * 1024)
#         if not chunck:
#             break
#         f.write(chunck)

blob = bucket.blob('opa_properties/opa.geojson')
blob.upload_from_string(response.read(), content_type = 'application/geojson')