resource "google_compute_network" "privatenet" {
  name                    = "privatenet"
  auto_create_subnetworks = "false"
}

resource "google_compute_subnetwork" "privatenet-us" {
  name          = "privatenet-us"
  region        = "us-central1"
  ip_cidr_range = "172.16.0.0/24"
  network       = google_compute_network.privatenet.self_link
}

resource "google_compute_subnetwork" "privatenet-eu" {
  name          = "privatenet-eu"
  region        = "europe-west1"
  ip_cidr_range = "172.20.0.0/24"
  network       = google_compute_network.privatenet.self_link
}

resource "google_compute_firewall" "privatenet-allow-http-ssh-rdp-icmp" {
  name    = "privatenet-allow-http-ssh-rdp-icmp"
  network = google_compute_network.privatenet.self_link

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "22", "3389"]
  }
}

module "privatenet-us-vm" {
  source              = "./instance"
  instance_name       = "privatenet-us-vm"
  instance_zone       = "us-central1-a"
  instance_subnetwork = google_compute_subnetwork.privatenet-us.self_link
}