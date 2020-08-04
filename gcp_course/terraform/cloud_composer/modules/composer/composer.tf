resource "google_composer_environment" "composer_env" {
  name     = var.service_name
  region   = var.region
  project  = var.project_id
  provider = google-beta

  config {
    node_count = var.node_count

    node_config {
      zone         = var.zone
      machine_type = var.machine_type
      disk_size_gb = var.disk_size_gb
      network      = google_compute_network.composer_test_network.id
      subnetwork   = google_compute_subnetwork.composer_test_subnetwork.id

      ip_allocation_policy {
        use_ip_aliases                = "true"
      }

      service_account = google_service_account.service_account.name
    }

    private_environment_config {
      enable_private_endpoint = "true"
    }

    web_server_network_access_control {
      allowed_ip_range {
        value = "108.211.106.249/32"
      }
    }

  }

  depends_on = [
    google_project_iam_member.composer_worker,
    google_compute_network.composer_test_network,
    google_compute_subnetwork.composer_test_subnetwork,
    google_compute_firewall.composer_test_firewall,
  ]
}

resource "google_compute_network" "composer_test_network" {
  name                    = "composer-test-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "composer_test_subnetwork" {
  name          = "composer-test-subnetwork"
  ip_cidr_range = "10.2.0.0/24"
  region        = "us-central1"
  network       = google_compute_network.composer_test_network.id
}

resource "google_service_account" "service_account" {
  account_id   = "composer-env-account"
  display_name = "composer-env-account"
  project      = var.project_id
}

resource "google_project_iam_member" "composer_worker" {
  role    = "roles/composer.worker"
  member  = "serviceAccount:${google_service_account.service_account.email}"
  project = var.project_id
}

resource "google_compute_firewall" "composer_test_firewall" {
    name = "composer-test-firewall"
    network = google_compute_network.composer_test_network.name

    allow {
        protocol = "all"
    }

    source_ranges = [
      "10.0.0.0/12",
      "10.2.0.0/24",
      "172.17.0.0/21",
      "172.17.8.0/21",
      "172.16.0.0/28",
      "172.16.20.0/23",
      "172.31.245.0/24",
    ]

    depends_on = [
      google_compute_network.composer_test_network,
    ]
}