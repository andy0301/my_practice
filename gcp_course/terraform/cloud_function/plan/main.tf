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

module "my_cloudfunction" {
  source                = "../modules/cloudfunctions"
  bucket_name           = "andy-00000002-bucket"
  function_name         = "load-gcs-to-bq"
  project_id            = local.project
  region                = local.region
  source_archive_bucket = "andy-00000002-bucket"
  source_archive_object = "load-gcs-to-bq.zip"
  available_memory_mb   = "512"
  dataset_id            = "andy_test_dataset"
  table_name            = "log1"
  file_name_prefix      = "api/api-"
}
