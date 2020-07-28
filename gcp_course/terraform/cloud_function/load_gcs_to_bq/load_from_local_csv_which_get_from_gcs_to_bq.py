#!/usr/bin/env python3

from google.cloud import bigquery
from google.cloud import storage
import logging
import tempfile
import os
import re
import sys
import warnings

logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(levelname)s: %(message)s')
warnings.filterwarnings('ignore')


def get_env_var(key):
    value = os.environ.get(key)
    if value is None:
        logging.error('{} is not set in the environment variables')
        sys.exit(1)
    return value


def set_tempfile_name():
    temp_file = tempfile.NamedTemporaryFile()
    return temp_file.name


def generate_csv(csv_output_file, csv_source_data):
    with open(csv_output_file, "w") as csv_output:
        csv_output.writelines(csv_source_data)
    logging.info("CSV output path: {}".format(csv_output))


def load_csv_to_bq(csv_file):
    dataset_name = get_env_var('DATASET_ID')
    table_name = get_env_var('TABLE_NAME')
    client = bigquery.Client()

    dataset_ref = client.dataset(dataset_name)
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    job_config.source_format = bigquery.SourceFormat.CSV

    with open(csv_file, 'rb') as source_file:
        load_job = client.load_table_from_file(
            source_file, dataset_ref.table(table_name), job_config=job_config
        )  # API request
    logging.info("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    logging.info("Job finished.")

    destination_table = client.get_table(dataset_ref.table(table_name))
    logging.info("Loaded {} rows.".format(destination_table.num_rows))


def on_gcs_trigger(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    logging.info('Event ID: {}'.format(context.event_id))
    logging.info('Event type: {}'.format(context.event_type))
    logging.info('Bucket: {}'.format(data['bucket']))
    logging.info('File: {}'.format(data['name']))
    logging.info('Metageneration: {}'.format(data['metageneration']))
    logging.info('Created: {}'.format(data['timeCreated']))
    logging.info('Updated: {}'.format(data['updated']))

    file_prefix = get_env_var('FILE_NAME_PREFIX')
    if not re.match(file_prefix, data['name']):
        logging.info("This function is only taking care of {} logs.".format(file_prefix))
        sys.exit(0)

    gcs_client = storage.Client()
    bucket = gcs_client.bucket(data['bucket'])
    blob = bucket.get_blob(data['name'])
    csv_arr = []

    for line in blob.download_as_string().decode('UTF-8').split("\n"):
        if not line:
            continue
        csv_row = line.replace("]", "").replace("[", "").replace("\"", "").replace(" ", ",")
        csv_arr.append(csv_row + "\n")

    csv_file = set_tempfile_name()
    generate_csv(csv_file, csv_arr)
    load_csv_to_bq(csv_file)
