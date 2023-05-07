from urllib.request import urlopen
from google.cloud import storage
import functions_framework

@functions_framework.http
def extract_assessment(request):
    client = storage.Client()
    bucket = client.bucket("musa509s23_team02_raw_data")
   
    url = "https://phl.carto.com/api/v2/sql?format=geojson&skipfields=cartodb_id&q=SELECT%20*%20FROM%20assessments"
    filename = 'assessments.csv'

    response = urlopen(url)
    blob = bucket.blob('opa_assessments/assessments.csv')
    blob.upload_from_string(response.read(), content_type='application/csv')
    
    return 'OK'






