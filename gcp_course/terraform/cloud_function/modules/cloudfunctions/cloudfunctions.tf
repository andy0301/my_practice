resource "google_cloudfunctions_function" "cloudfunctions_function" {
  name                = var.function_name
  description         = "Cloud functions"
  project             = var.project_id
  region              = var.region
  runtime             = "python37"
  available_memory_mb = var.available_memory_mb


  source_archive_bucket = var.source_archive_bucket
  source_archive_object = var.source_archive_object
  entry_point           = "on_gcs_trigger"
  service_account_email = google_service_account.service_account.email

  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = var.bucket_name
  }

  environment_variables = {
    DATASET_ID = var.dataset_id
    TABLE_NAME = var.table_name
    FILE_NAME_PREFIX = var.file_name_prefix

  }

  depends_on = [
    google_service_account.service_account,
  ]

}

resource "google_service_account" "service_account" {
  account_id   = "cf-service-account"
  display_name = "cf-service-account"
  project      = var.project_id
}

resource "google_project_iam_member" "bq_data_editor" {
  member  = "serviceAccount:${google_service_account.service_account.email}"
  project = var.project_id
  role    = "roles/bigquery.dataEditor"
}

resource "google_project_iam_member" "bq_data_owner" {
  member  = "serviceAccount:${google_service_account.service_account.email}"
  project = var.project_id
  role    = "roles/bigquery.dataOwner"
}

resource "google_project_iam_member" "bq_user" {
  member  = "serviceAccount:${google_service_account.service_account.email}"
  project = var.project_id
  role    = "roles/bigquery.user"
}

resource "google_project_iam_member" "bq_job_user" {
  member  = "serviceAccount:${google_service_account.service_account.email}"
  project = var.project_id
  role    = "roles/bigquery.jobUser"
}

resource "google_project_iam_member" "storage_viewer" {
  member  = "serviceAccount:${google_service_account.service_account.email}"
  project = var.project_id
  role    = "roles/storage.objectViewer"
}
