import pathlib
from google.cloud import bigquery
import functions_framework

DIR = pathlib.Path(__file__).parent


@functions_framework.http

def load_opa_properties(event, context):
    # Set up BigQuery clients
    bq_client = bigquery.Client()

    # Set up table references
    source_dataset_ref = bq_client.dataset('source')
    source_table_ref = source_dataset_ref.table('opa_properties')
    core_dataset_ref = bq_client.dataset('core')
    core_table_ref = core_dataset_ref.table('opa_properties')

    # Set up external table schema
    external_table_schema = [
        bigquery.SchemaField('parcel_number', 'STRING'),
        bigquery.SchemaField('address', 'STRING'),
        bigquery.SchemaField('zipcode', 'STRING'),
        bigquery.SchemaField('owner', 'STRING'),
        # Add any other fields as needed
    ]

    # Set up external table configuration
    external_config = bigquery.ExternalConfig('NEWLINE_DELIMITED_JSON')
    external_config.schema = external_table_schema
    external_config.source_uris = ['gs://musa509s23_team02_prepared_data/opa_properties/data.jsonl']

    # Create or update external table
    external_table = bigquery.Table(source_table_ref, external_config)
    external_table.create_or_replace()

    # Set up internal table schema
    internal_table_schema = [
        bigquery.SchemaField('property_id', 'STRING'),
        bigquery.SchemaField('parcel_number', 'STRING'),
        bigquery.SchemaField('address', 'STRING'),
        bigquery.SchemaField('zipcode', 'STRING'),
        bigquery.SchemaField('owner', 'STRING'),
        # Add any other fields as needed
    ]

    # Create or update internal table
    internal_table = bigquery.Table(core_table_ref, schema=internal_table_schema)
    internal_table.create_or_replace()

    # Populate internal table from external table
    insert_query = f"""
        INSERT INTO `{core_dataset_ref.project}.{core_dataset_ref.dataset_id}.opa_properties`
        SELECT
            parcel_number AS property_id,
            *
        FROM `{source_dataset_ref.project}.{source_dataset_ref.dataset_id}.opa_properties`
    """
    query_job = bq_client.query(insert_query)
    query_job.result()

    print('Load OPA Properties completed.')
