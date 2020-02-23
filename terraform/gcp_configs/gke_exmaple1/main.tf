provider "google" {
  credentials = file("../../green-reporter-266619-556d55fdbcea.json")
  project     = "green-reporter-266619"
  region      = "us-central1"
  zone        = "us-central1-c"
}

#resource "google_project_service" "kubernetes" {
#  project = "green-reporter-266619"
#  service = "container.googleapis.com"
#}

resource "google_container_cluster" "gke_example1" {
  name     = "gke-example1"
  location = "us-central1"

  remove_default_node_pool = true
  initial_node_count       = 1

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }
}

resource "google_container_node_pool" "gke_example1_nodes" {
  name       = "gke-example1-node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.gke_example1.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "n1-standard-1"

    metadata = {
      disable-legacy-endpoints = "true"
    }

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }
}