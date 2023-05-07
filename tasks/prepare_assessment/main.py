import csv
import io
import json
from google.cloud import storage
import functions_framework


@functions_framework.http
def prepare_assessments(request):
    client = storage.Client()
    raw_bucket =  client.bucket("musa509s23_team02_prepared_data")
    processed_bucket =client.bucket("musa509s23_team02_prepared_data")
    raw_blob = raw_bucket.blob("opa_assessments/assessments.csv")
    processed_blob = processed_bucket.blob('opa_assessments/assessments.csv')

    content = raw_blob.download_as_string()
    data = json.loads(content)
    outfile = io.StringIO()
    writer = csv.writer(outfile)
    writer.writerows(data)
    processed_blob.upload_from_string(outfile.getvalue(), content_type = "text/csv")
    
    return 'OK'



