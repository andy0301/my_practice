#!/usr/bin/env python

from google.cloud import bigquery
import string
import sys
import random
import time

def table_name_generator():
    random_str = ''.join(random.choice(string.ascii_lowercase) for x in range(8))
    timestamp = str(time.time()).replace('.','_')
    return "{}_{}".format(random_str, timestamp)

def insert_table_query_generator(source_table_id, dest_table_id):
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
    """.format(dest_table_id, source_table_id)
    return query


def main ():

    log_uri = "gs://andy-00000002-bucket/api/api-test.log"
    #log_uri = "gs://andy-00000002-bucket/envoy/api/api-0kg1-application-http-egress-2020-07-27-06-25-11.log"
    client = bigquery.Client()
    dataset_ref = client.dataset("service_log_parser")
    print(dataset_ref.table('envoy_access_log'))
    dataset_id = "service_log_parser"
    project_id = "green-reporter-266619"
    table_name = table_name_generator()
    table_id = project_id + '.' + dataset_id + '.' + table_name
    #dest_table_id = project_id + '.' + dataset_id + '.' + 'envoy_access_log'
    dest_table_id = '{}.{}'.format(dataset_id, 'envoy_access_log')
    insert_sql = insert_table_query_generator(table_name, dest_table_id)
    #print(insert_sql)

    external_config = bigquery.ExternalConfig("CSV")
    external_config.source_uris = [
        log_uri,
    ]
    external_config.schema = [
        bigquery.SchemaField("content", "STRING", mode="REQUIRED"),
    ]
    job_config = bigquery.QueryJobConfig(table_definitions={table_name: external_config})
    query_job = client.query(insert_sql, job_config=job_config) 
    if len(list(query_job)) == 0: # Waits for query to finish
        print("Load data completed!")

if __name__ == "__main__":
    main()


