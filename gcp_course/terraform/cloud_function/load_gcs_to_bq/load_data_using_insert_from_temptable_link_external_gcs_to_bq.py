#!/usr/bin/env python3

from google.cloud import bigquery
import logging
import os
import random
import re
import string
import sys
import time
import warnings

logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(levelname)s: %(message)s')
warnings.filterwarnings('ignore')


def get_env_var(key):
    value = os.environ.get(key)
    if value is None:
        logging.error('{} is not set in the environment variables')
        sys.exit(1)
    return value


def table_name_generator():
    random_str = ''.join(random.choice(string.ascii_lowercase) for x in range(8))
    timestamp = str(time.time()).replace('.', '_')
    return "{}_{}".format(random_str, timestamp)


def insert_table_query_generator(source_table_id, target_table_id):
    query = """
        INSERT INTO `{}`
        SELECT TIMESTAMP(SPLIT(REPLACE(REPLACE(CONTENT, "[", ""), "]", ""), ' ') [ORDINAL(1)])
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(2)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(3)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(4)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(5)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(6)]
        , CAST(SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(7)] AS INT64)
        , CAST(SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(8)] AS INT64)
        , CAST(SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(9)] AS INT64)
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(10)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(11)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(12)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(13)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(14)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(15)]
        , SPLIT(REPLACE(CONTENT, '"', ''), ' ') [ORDINAL(16)]
        FROM `{}`
    """.format(target_table_id, source_table_id)
    return query


def load_gcs_to_bq(log_uri):
    dataset_id = get_env_var('DATASET_ID')
    target_table_name = get_env_var('TABLE_NAME')
    client = bigquery.Client()

    temp_table_name = table_name_generator()
    target_table_id = '{}.{}'.format(dataset_id, target_table_name)
    insert_sql = insert_table_query_generator(temp_table_name, target_table_id)

    external_config = bigquery.ExternalConfig("CSV")
    external_config.source_uris = [
        log_uri,
    ]
    external_config.schema = [
        bigquery.SchemaField("content", "STRING", mode="REQUIRED"),
    ]
    job_config = bigquery.QueryJobConfig(table_definitions={temp_table_name: external_config})
    query_job = client.query(insert_sql, job_config=job_config)
    if len(list(query_job)) == 0:
        print("Load {} to {} completed!".format(log_uri, target_table_id))


def on_gcs_trigger(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
        
    NOTE:
        The function executes only for envoy/api/api-* logs.
        Will skip other files which uploaded to same bucket.
    """

    file_prefix = get_env_var('FILE_NAME_PREFIX')
    if re.match(file_prefix, data['name']):
        logging.info('Event ID: {}'.format(context.event_id))
        logging.info('Event type: {}'.format(context.event_type))
        logging.info('Bucket: {}'.format(data['bucket']))
        logging.info('File: {}'.format(data['name']))
        logging.info('Metageneration: {}'.format(data['metageneration']))
        logging.info('Created: {}'.format(data['timeCreated']))
        logging.info('Updated: {}'.format(data['updated']))

        log_uri = "gs://{}/{}".format(data['bucket'], data['name'])
        logging.info("Start loading {} to Big Query ...".format(log_uri))
        load_gcs_to_bq(log_uri)
