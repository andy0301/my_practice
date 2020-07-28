#!/usr/bin/env python3

from google.cloud import bigquery
from google.cloud import storage
import logging
import tempfile
import os
import re
import sys
import warnings
from datetime import datetime

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
    logging.info("CSV Ouput: {}".format(csv_output_file))


def load_csv_to_bq(csv_file):
    dataset_name = get_env_var('DATASET_ID')
    table_name = get_env_var('TABLE_NAME')
    client = bigquery.Client()

    dataset_ref = client.dataset(dataset_name)
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
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


def load_json_to_bq(json_arr):
    logging.info("bq 1 ... {}".format(datetime.now()))
    dataset_name = get_env_var('DATASET_ID')
    table_name = get_env_var('TABLE_NAME')
    client = bigquery.Client()

    dataset_ref = client.dataset(dataset_name)
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    job_config.source_format = bigquery.SourceFormat.CSV
    
    logging.info("Starting load from json ...")
    load_job = client.load_table_from_json(
        json_arr, dataset_ref.table(table_name), job_config=job_config
    )  # API request
    logging.info("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    logging.info("Job finished.")

    destination_table = client.get_table(dataset_ref.table(table_name))
    logging.info("Loaded {} rows.".format(destination_table.num_rows))


def on_gcs_trigger():
    file_name = "envoy/api/envoy_api_api-g525-application-http-egress-2020-07-23-06-25-06.log"
    bucket_name = "andy-00000002-bucket"
    file_prefix = get_env_var('FILE_NAME_PREFIX')
    print("starting ... at {}".format(datetime.now()))
    if not re.match(file_prefix, file_name):
        logging.info("This function is only taking care of {} logs.".format(file_prefix))
        sys.exit(0)

    gcs_client = storage.Client()
    bucket = gcs_client.bucket(bucket_name)
    blob = bucket.get_blob(file_name)
    #csv_arr = []
    json_arr = []
    print(datetime.now()) 
    lines = list(blob.download_as_string().decode('UTF-8').split("\n"))
    print("lines created at: {}".format(datetime.now()))
    for line in lines:
    #for line in blob.download_as_string().decode('UTF-8').split("\n"):
        if not line:
            continue

        dict = {}
        arr = list(line.split())
        dict["start_time"] = arr[0].replace("]", "").replace("[", "")
        dict["method"] = arr[1].replace("\"", "")
        dict["path"] = arr[2].replace("\"", "")
        dict["protocol"] = arr[3].replace("\"", "")
        dict["response_code"] = arr[4].replace("\"", "")
        dict["response_flags"] = arr[5].replace("\"", "")
        dict["bytes_received"] = arr[6].replace("\"", "")
        dict["bytes_sent"] = arr[7].replace("\"", "")
        dict["duration"] = arr[8].replace("\"", "")
        dict["resp_x_envoy_upstream_service_time"] = arr[9].replace("\"", "")
        dict["req_x_forwarded_for"] = arr[10].replace("\"", "")
        dict["req_user_agent"] = arr[11].replace("\"", "")
        dict["req_x_request_id"] = arr[12].replace("\"", "")
        dict["downstream_remote_addr_without_port"] = arr[13].replace("\"", "")
        dict["upstream_host"] = arr[14].replace("\"", "")
        dict["customer_id"] = arr[15].replace("\"", "")
        #print(datetime.now())
        json_arr.append(dict)
        #break
#        csv_row = line.replace("]", "").replace("[", "").replace("\"", "").replace(" ", ",")
#        csv_arr.append(csv_row + "\n")

#    csv_file = set_tempfile_name()
#    generate_csv(csv_file, csv_arr)
    #load_csv_to_bq(csv_file)

    #print(json_arr)
    load_json_to_bq(json_arr)

if __name__ == "__main__":
    on_gcs_trigger()
