output "db_instance_name" {
  value       = google_sql_database_instance.lab_instance.name
  description = "Instance name"
}

output "db_instance_selflink" {
  value       = google_sql_database_instance.lab_instance.self_link
  description = "Instnace self_link"
}

output "db_instance_ip_address" {
  value       = google_sql_database_instance.lab_instance.ip_address
  description = "Instance IP address"
}


