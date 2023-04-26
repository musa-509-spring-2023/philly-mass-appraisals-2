import pathlib
from google.cloud import bigquery
import functions_framework
import dotenv
dotenv.load_dotenv()

DIR = pathlib.Path(__file__).parent


@functions_framework.http
def load_opa_assessments(request):
    client = bigquery.Client()

    with open(DIR / 'source_opa_assess.sql') as f:
        sql = f.read()
    job = client.query(sql)
    job.result()

    with open(DIR / 'core_opa_assess.sql') as f:
        sql = f.read()
    job = client.query(sql)
    job.result()

    return 'OK'