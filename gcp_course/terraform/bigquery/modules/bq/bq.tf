resource "google_bigquery_dataset" "bq_dataset" {
    dataset_id = var.dataset_id
    friendly_name = var.friendly_name
    description = var.description
    location = var.location
    project = var.project_id
    default_table_expiration_ms = var.default_table_expiration_ms

    labels = {
        env = var.env
    }
}