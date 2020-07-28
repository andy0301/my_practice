locals {
  project = "green-reporter-266619"
  region  = "us-central1"
  zone    = "us-central1-c"
}

provider "google" {
  credentials = file("../../green-reporter-266619-5b0288dea60a.json")
  project     = local.project
  region      = local.region
  zone        = local.zone
}

module "my_test_bq_dataset" {
  source      = "../modules/bq"
  location    = "US"
  project_id  = local.project
  dataset_id = "andy_test_dataset"
  friendly_name = "my_test"
  description = "This is a test dataset!"
  env = "test"
}

resource "google_bigquery_table" "log1" {
    dataset_id = module.my_test_bq_dataset.dataset_id
    table_id = "log1"

    labels = {
        env = "test"
    }

    time_partitioning {
        type = "DAY"
        field = "start_time"
    }

    schema = <<EOF
[
    {
        "name": "start_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "start time"
    },
    {
        "name": "method",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "http method"
    },
    {
        "name": "path",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "http uri path"
    },
    {
        "name": "protocol",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "protocol"
    },
    {
        "name": "response_code",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "http response code"
    },
    {
        "name": "response_flags",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "http response flags"
    },
    {
        "name": "bytes_received",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "bytes received"
    },
    {
        "name": "bytes_sent",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "bytes sent"
    },
    {
        "name": "duration",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "duration"
    },
    {
        "name": "resp_x_envoy_upstream_service_time",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "RESP-X-ENVOY-UPSTREAM-SERVICE-TIME"
    },
    {
        "name": "req_x_forwarded_for",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "REQ-X-FORWARDED-FOR"
    },
    {
        "name": "req_user_agent",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "REQ-USER-AGENT"
    },
    {
        "name": "req_x_request_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "REQ-X-REQUEST-ID"
    },
    {
        "name": "downstream_remote_addr_without_port",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "DOWNSTREAM_REMOTE_ADDRESS_WITHOUT_PORT"
    },
    {
        "name": "upstream_host",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "UPSTREAM_HOST"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "REQ_CUSTOMER_ID"
    }
]
EOF

}
