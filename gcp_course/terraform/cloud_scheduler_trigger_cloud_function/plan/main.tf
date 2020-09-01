data "google_storage_bucket_object" "function_source_artifact" {
  bucket = "andy-00000002-bucket"
  name   = "cloud_functions/zookeeper_backup_001.zip"
}

locals {
  project = "green-reporter-266619"
  region  = "us-central1"
  zone    = "us-central1-c"
}

module "cloudscheduler_trigger_cloudfunction" {
  available_memory_mb   = 256
  bucket_name           = "andy-00000002-bucket"
  host                  = "34.123.5.203:2181"
  nodes                 = "/andy/config"
  project_id            = "${local.project}"
  region                = "${local.region}"
  source_archive_bucket = "${data.google_storage_bucket_object.function_source_artifact.bucket}"
  source_archive_object = "${data.google_storage_bucket_object.function_source_artifact.name}"
  source                = "../modules/cs_trigger_cf"
}

provider "google" {
  credentials = "${file("../../green-reporter-266619-5b0288dea60a.json")}"
  project     = "${local.project}"
  region      = "${local.region}"
  version     = "~> 2.20.3"
}

# resource "google_project_services" "project_services" {
#  project = "${local.project}"


#  services = [
#    "appengine.googleapis.com",
#    "cloudscheduler.googleapis.com",
#    "pubsub.googleapis.com",
#    "serviceusage.googleapis.com",
#  ]
# }

