provider "google" {
  credentials = file("../../green-reporter-266619-5b0288dea60a.json")
  project     = var.project
  region      = var.region
  zone        = var.zone
}

module "lab_cloud_mysql_instance" {
  source            = "../modules/cloudsql"
  region            = "us-east4"
  tier              = "db-f1-micro"
  database_version  = "MYSQL_5_7"
  sql_user_password = "abc123"
}