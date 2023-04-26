import pathlib
from google.cloud import bigquery
import functions_framework
import dotenv
dotenv.load_dotenv()

DIR = pathlib.Path(__file__).parent


@functions_framework.http
def load_properties(request):
    client = bigquery.Client()

    with open(DIR / 'update_source_opa_properties.sql') as f:
        sql = f.read()
    job = client.query(sql)
    job.result()

    with open(DIR / 'update_core_opa_properties.sql') as f:
        sql = f.read()
    job = client.query(sql)
    job.result()

    return 'OK'
