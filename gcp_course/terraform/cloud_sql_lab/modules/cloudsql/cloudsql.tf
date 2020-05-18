resource "google_sql_database_instance" "lab_instance" {
  name             = "lab-instance"
  database_version = var.database_version
  region           = var.region


  settings {
    # Second-generation instance tiers are based on the machine
    # type. See argument reference below.
    tier      = var.tier
    disk_size = var.disk_size
  }

}

resource "random_id" "user_password" {
  keepers = {
    # Generate a new id each time we generate new sql_database_instance
    name = google_sql_database_instance.lab_instance.name
  }

  byte_length = 8
}

resource "random_id" "user_name_suffix" {
  byte_length = 4
}

resource "google_sql_user" "lab_instance_user" {
  name     = var.sql_user_name == "" ? "test-user-${random_id.user_name_suffix.hex}" : var.sql_user_name
  instance = google_sql_database_instance.lab_instance.name
  password = var.sql_user_password == "" ? random_id.user_password.hex : var.sql_user_password
}

resource "google_sql_database" "lab_db" {
  name     = "lab-test-db"
  instance = google_sql_database_instance.lab_instance.name
}
