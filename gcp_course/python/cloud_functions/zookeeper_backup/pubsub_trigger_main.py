#!/usr/bin/env python

from datetime import datetime
from kazoo.client import KazooClient, NoNodeError
from google.cloud import storage
import json
import logging
import os
import sys

def get_env_var(key):
    value = os.environ.get(key)
    if value is None:
        logging.error('{} is not set in the environment variables')
        sys.exit(1)
    return value


def set_backup_file_name(backup_node):
    backup_date = datetime.now().strftime('%Y%m%d-%H%M')
    backup_node_name = backup_node.replace('/', '-')
    backup_file_name = "zk-backup{}-{}.json".format(backup_node_name, backup_date)
    return backup_file_name


def output_to_json_file(file_name, file_data):
    with open(file_name, 'w') as jf:
        json.dump(file_data, jf)


def output_to_file(data):
    file = "/tmp/list_zk_node.txt"
    with open(file, 'a') as f:
        f.write("{}\n".format(data))


def get_sub_zk_nodes(zk_client, zk_node):
    sub_zk_nodes = []

    try:
        children = zk_client.get_children(zk_node)
    except NoNodeError:
        logging.error("Fail to get children, node: {} is not in zookeeper.".format(zk_node))
        return None

    for child in children:
        sub_zk_nodes.append("{}/{}".format(zk_node, child))
    return sub_zk_nodes


def get_node_data(zk_client, zk_node):
    try:
        data, state = zk_client.get(zk_node)
    except NoNodeError:
        logging.error("Fail to get node data, node: {} is not in zookeeper.".format(zk_node))
        return None
    return data.decode('UTF-8')


def dump_backup_data_to_dict(zk_client, zk_node, zk_backup_dict):
    sub_zk_nodes = get_sub_zk_nodes(zk_client, zk_node)
    zk_nodes_array = []
    
    if zk_client.exists(zk_node).numChildren == 0:
        zk_data_dict = {}
        data = get_node_data(zk_client, zk_node)
        zk_data_dict[zk_node] = data
        zk_nodes_array.append(zk_data_dict)
    else:
        for node in sub_zk_nodes:
            zk_data_dict = {}

            if zk_client.exists(node).numChildren == 0:
                data = get_node_data(zk_client, node)
                zk_data_dict[node] = data
                zk_nodes_array.append(zk_data_dict)

            if zk_client.exists(node).numChildren > 0:
                dump_backup_data_to_dict(zk_client, node, zk_backup_dict)

    if zk_nodes_array:
        zk_backup_dict[zk_node] = zk_nodes_array


def backup_zookeeper_node(zk_client, zk_node):
    zk_client.start()
    zk_backup_dict = {}

    try:
        backup_file_name = set_backup_file_name(zk_node)
        first_line_nodes = get_sub_zk_nodes(zk_client, zk_node)
        data = get_node_data(zk_client, zk_node)
        if data:
            zk_backup_dict[zk_node] = data
        for node in first_line_nodes:
            dump_backup_data_to_dict(zk_client, node, zk_backup_dict)
        output_to_json_file(backup_file_name, zk_backup_dict)
    except Exception as e:
        raise('Failed to backup to {}. Error = {}'.format(backup_file_name, str(e)))
    finally:
        zk_client.stop()

    try:
        backup_bucket = get_env_var('BUCKET')
        client = storage.Client()
        bucket = client.get_bucket(backup_bucket)
        blob = bucket.blob(backup_file_name)
        blob.upload_from_filename(backup_file_name)
    except Exception as e:
       logging.error("Upload backup: {} to gs://{} failed.".format(backup_file_name, backup_bucket))


def main(event, context):
# def main():
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """
    zk_host = get_env_var('HOST')
    root_nodes = get_env_var('NODES').split(',')
    
    log_level = "INFO"
    logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s: %(message)s", level=log_level, stream=sys.stderr)
    logging.info("Starting backup zookeeper data ...")
    zk_client = KazooClient(hosts=zk_host, read_only=True, timeout=10)
    for root in root_nodes:
        logging.info("Starting backup zk node: {} ... ".format(root))
        backup_zookeeper_node(zk_client, root)
        logging.info("Backup zk node: {} ... [COMPLETED]".format(root))


# if __name__ == "__main__":
#    main()
