resource "google_storage_bucket" "gcs_bucket" {
    name = var.bucket_name
    project = var.project_id
    location = var.location
    force_destroy = true

    versioning {
        enabled = true
    }
}