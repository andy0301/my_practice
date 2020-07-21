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

module "my_test_bucket" {
  source      = "../modules/gcs"
  location    = "US"
  project_id  = local.project
  bucket_name = "andy-00000002-bucket"
}