from urllib.request import urlopen
from google.cloud import storage
import functions_framework
import dotenv
dotenv.load_dotenv()


@functions_framework.http
def extract_properties(request):
    client = storage.Client()
    bucket = client.bucket("musa509s23_team02_raw_data")

    url = "https://phl.carto.com/api/v2/sql?filename=opa_properties_public&format=geojson&skipfields=cartodb_id&q=SELECT+*+FROM+opa_properties_public"
    response = urlopen(url)

    blob = bucket.blob('opa_properties/opa.geojson')
    blob.upload_from_string(response.read(), content_type='application/geojson')

    return 'OK'
