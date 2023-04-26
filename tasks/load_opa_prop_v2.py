import pathlib
from google.cloud import bigquery
import functions_framework

DIR = pathlib.Path(__file__).parent


@functions_framework.http

def load_opa_properties(event, context):
    # Set up BigQuery clients
    bq_client = bigquery.Client()

    # Set up table references
    #source_dataset_ref = bq_client.dataset('source')
    #source_table_ref = source_dataset_ref.table('opa_properties')
    #core_dataset_ref = bq_client.dataset('core')
    #core_table_ref = core_dataset_ref.table('opa_properties')

    with open(DIR / 'create_opa_properties_external.sql') as external_f:
        sql = external_f.read()
        query_job = bq_client.query(sql)
        query_job.result()

    with open(DIR / 'create_opa_properties_internal.sql') as internal_f:
        sql = internal_f.read()
        query_job = bq_client.query(sql)
        query_job.result()    

    return 'Load OPA Properties completed.'