def generate_assessment_chart_configs(request):
    project_id = os.environ.get('GCP_PROJECT')
    dataset_id = derived
    table_id = 'current_assessment_bins'

    client = bigquery.Client()
    table = client.get_table(f'{project_id}.{dataset_id}.{table_id}')
    table = client.get_table(table_ref)

    query = f'SELECT * FROM `{project_id}.{dataset_id}.{table_id}`'
    query_job = client.query(query)
    rows = query_job.result()

    results = []
    for row in rows:
        results.append({
        'tax_year': row['tax_year'],
        'lower_bound': row['lower_bound'],
        'upper_bound': row['upper_bound'],
        'property_count': row['property_count']
        })

json_filename = 'tax_year_assessment_bins.json'
with open(json_filename, 'w') as f:
    json.dump(results, f)


bucket_name = 'musa509s23_team02_public'
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(f'/assessment_bins/{json_filename}')
blob.upload_from_filename(json_filename)

return 'JSON file generated and uploaded to GCS.', 200 