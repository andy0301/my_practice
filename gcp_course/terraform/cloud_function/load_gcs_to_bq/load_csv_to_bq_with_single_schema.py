#!/usr/bin/env python3

from google.cloud import bigquery

def load_gcs_to_bq (uri):
    client = bigquery.Client()
    log_uri = uri
    print(log_uri)

    dataset_ref = client.dataset("andy_test_dataset")
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    job_config.source_format = bigquery.SourceFormat.CSV

    load_job = client.load_table_from_uri(
      log_uri, dataset_ref.table("log1"), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = client.get_table(dataset_ref.table("log1"))
    print("Loaded {} rows.".format(destination_table.num_rows))

def on_gcs_trigger(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    print('Metageneration: {}'.format(data['metageneration']))
    print('Created: {}'.format(data['timeCreated']))
    print('Updated: {}'.format(data['updated']))

    uri = "gs://{}/{}".format(data['bucket'],data['name'])
    load_gcs_to_bq(uri)