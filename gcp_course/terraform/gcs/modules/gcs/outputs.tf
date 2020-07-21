output "bucket_id" {
    value = google_storage_bucket.gcs_bucket.id
}

output "bucket_name" {
    value = google_storage_bucket.gcs_bucket.name
}

output "bucket_self_link" {
    value = google_storage_bucket.gcs_bucket.self_link
}