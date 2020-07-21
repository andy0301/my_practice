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

    schema = <<EOF
[
    {
        "name": "content",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "test table"
    }
]
EOF

}