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

provider "google-beta" {
  credentials = file("../../green-reporter-266619-5b0288dea60a.json")
  project     = local.project
  region      = local.region
  zone        = local.zone
}

module "my_cloud_composer_test" {
  source       = "../modules/composer"
  service_name = "my-test-composer"
  region       = local.region
  project_id   = local.project
  node_count   = 3
  zone         = local.zone
  machine_type = "n1-standard-1"
  disk_size_gb = 20
}