provider "google" {
  credentials = file("../test_packer/green-reporter-266619-11ba8b4884e5.json")
  project     = "green-reporter-266619"
  region      = "us-west1"
  zone        = "us-west1-b"
}

data "google_compute_image" "andy_test_image" {
    name = "u16demo-1584922593"
    project = "green-reporter-266619"
}

resource "google_compute_instance" "andy_test_1" {
  name         = "andy-test-1"
  machine_type = "n1-standard-1"
  zone         = "us-west1-b"

  tags = ["foo", "bar"]

  boot_disk {
    initialize_params {
      image = data.google_compute_image.andy_test_image.self_link
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  metadata = {
    foo = "bar"
  }

  metadata_startup_script = "echo hi > /test.txt"
}
