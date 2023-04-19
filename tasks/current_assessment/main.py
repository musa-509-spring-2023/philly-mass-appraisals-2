import pathlib
from google.cloud import bigquery
import functions_framework

DIR = pathlib.Path(__file__).parent


@functions_framework.http
def load_data(request):
    client = bigquery.Client()

    with open(DIR / 'task9.sql') as f:
        sql = f.read()
    query_job = client.query(sql)
    query_job.result()

    return 'OK'
