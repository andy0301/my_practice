
resource "google_cloud_scheduler_job" "cloudfunction_job" {
  name        = "cloudfunction-job"
  description = "Trigger cloud function's job"
  project     = "${var.project_id}"

  http_target {
    http_method = "POST"
    uri         = "${google_cloudfunctions_function.cloudfunctions_function.https_trigger_url}"
  }

  region = "${var.region}"

  # every minute
  schedule = "0 0 * * *"
}

resource "google_service_account" "service_account" {
  account_id   = "cloudfunction-service-account"
  display_name = "cloudfunction-service-account"
  project      = "${var.project_id}"
}

resource "google_storage_bucket_iam_member" "storage_admin" {
  bucket = "${var.bucket_name}"
  member = "serviceAccount:${google_service_account.service_account.email}"
  role   = "roles/storage.objectAdmin"
}

# resource "google_vpc_access_connector" "connector" {
#  name          = "vpcconn"
#  ip_cidr_range = "10.128.0.0/20"
#  network       = "default"
#  region        = "${var.region}"
# }

resource "google_cloudfunctions_function" "cloudfunctions_function" {
  available_memory_mb = "${var.available_memory_mb}"

  depends_on = [
    "google_service_account.service_account",
  ]

  description = "Cloud Scheduler/PubSub trigger Cloud Function."
  entry_point = "main"

  environment_variables = {
    BACKUP_BUCKET = "${var.bucket_name}"
    HOST          = "${var.host}"
    NODES         = "${var.nodes}"
  }

  max_instances         = "${var.max_instances}"
  name                  = "cloudscheduler-http-trigger-function"
  project               = "${var.project_id}"
  region                = "${var.region}"
  runtime               = "python37"
  source_archive_bucket = "${var.source_archive_bucket}"
  source_archive_object = "${var.source_archive_object}"
  service_account_email = "${google_service_account.service_account.email}"
  timeout               = "${var.timeout}"
  trigger_http          = true
  # vpc_connector         = "${google_vpc_access_connector.connector.name}"
}

resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = "${google_cloudfunctions_function.cloudfunctions_function.project}"
  region         = "${google_cloudfunctions_function.cloudfunctions_function.region}"
  cloud_function = "${google_cloudfunctions_function.cloudfunctions_function.name}"

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}