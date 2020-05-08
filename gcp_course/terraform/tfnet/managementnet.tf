resource "google_compute_network" "managementnet" {
  name                    = "managementnet"
  auto_create_subnetworks = "false"
}

resource "google_compute_subnetwork" "managementsubnet-us" {
  name          = "managementsubnet-us"
  region        = "us-central1"
  ip_cidr_range = "10.130.0.0/20"
  network       = google_compute_network.managementnet.self_link
}

resource "google_compute_firewall" "managementnet-allow-http-ssh-rdp-icmp" {
  name    = "managementnet-allow-http-ssh-rdp-icmp"
  network = google_compute_network.managementnet.self_link

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "22", "3389"]
  }
}

module "managementnet-us-vm" {
  source              = "./instance"
  instance_name       = "managementnet-us-vm"
  instance_zone       = "us-central1-a"
  instance_subnetwork = google_compute_subnetwork.managementsubnet-us.self_link
}