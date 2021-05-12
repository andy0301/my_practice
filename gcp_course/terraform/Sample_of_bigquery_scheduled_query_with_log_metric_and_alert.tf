# Please create scheduled query firstly using terraform.
# Then we can use the name which return from google_bigquery_data_transfer_config in output,
# when creates logging metric.
resource "google_bigquery_data_transfer_config" "query_config" {
  display_name           = "query-name"
  data_source_id         = "scheduled_query"
  destination_dataset_id = google_bigquery_dataset.YOUR_DATASET.dataset_id
  location               = "US"
  params = {
    destination_table_name_template = "table name"
    write_disposition               = "WRITE_APPEND"
    query                           = "SELECT name FROM tabl WHERE x = 'y'"
  }
  schedule = "your query schedule time"
}

# Creates logging metric for scheduled query error counts.
# The scheduled query config return "google_bigquery_data_transfer_config.query_config.name"
# which like "projects/<project_id>/locations/us-east4/transferConfigs/<bigquery_scheduled_query_config_id>"
# will need just config id from above query_config.name to set filter, details see below terraform code
resource "google_logging_metric" "scheduled_query_count_metric" {
  filter = "resource.labels.config_id=\"${element(split("/", google_bigquery_data_transfer_config.query_config.name), length(split("/", google_bigquery_data_transfer_config.query_config.name)) - 1)}\" severity=\"ERROR\""
  metric_descriptor {
    metric_kind = "DELTA"
    value_type  = "INT64"
  }
  name    = "Your metrics name"
  project = var.project_id
}

# After above logging metric created, then create alert policy to setup alert.
resource "google_monitoring_alert_policy" "scheduled_query_alert_policy" {
  combiner = "OR"
  conditions {
    condition_threshold {
      aggregations {
        alignment_period   = "60s"
        per_series_aligner = "ALIGN_MEAN"
      }
      comparison      = "COMPARISON_GT"
      duration        = "60s"
      filter          = "metric.type=\"logging.googleapis.com/user/${google_logging_metric.scheduled_query_count_metric.name}\" resource.type=\"bigquery_dts_config\" resource.label.\"project_id\"=\"${var.project_id}\""
      threshold_value = 1
      trigger {
        count = 1
      }
    }
    display_name = "Define condition display name"
  }
  depends_on = [
    google_logging_metric.scheduled_query_count_metric,
  ]
  display_name = "Define policy display name"
  documentation {
    content   = "Runbook Url"
    mime_type = "text/markdown"
  }
  enabled = "true"
  notification_channels = [
    google_monitoring_notification_channel.notification_channel.id,
  ]
  project = var.project_id
}
