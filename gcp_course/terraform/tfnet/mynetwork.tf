resource "google_compute_network" "mynetwork" {
  name                    = "mynetwork"
  auto_create_subnetworks = "true"
}

resource "google_compute_firewall" "mynetwork-allow-http-ssh-rdp-icmp" {
  name    = "mynetwork-allow-http-ssh-rdp-icmp"
  network = google_compute_network.mynetwork.self_link

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "22", "3389"]
  }
}

module "mynetwork-us-vm" {
  source              = "./instance"
  instance_name       = "mynetwork-us-vm"
  instance_zone       = "us-central1-a"
  instance_subnetwork = google_compute_network.mynetwork.self_link
}

module "mynetwork-eu-vm" {
  source              = "./instance"
  instance_name       = "mynetwork-eu-vm"
  instance_zone       = "europe-west1-d"
  instance_subnetwork = google_compute_network.mynetwork.self_link
}