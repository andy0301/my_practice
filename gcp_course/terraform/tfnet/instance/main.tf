variable "instance_name" {
  description = "vm instance name"
}

variable "instance_zone" {
    description = "zone"
}

variable "instance_type" {
    description = "instance vm type"
    default = "n1-standard-1"
}

variable "instance_subnetwork" {
    description = "instance subnetwork"
}


resource "google_compute_instance" "vm_instance" {
    name = var.instance_name
    zone = var.instance_zone
    machine_type = var.instance_type

    boot_disk {
        initialize_params {
            image = "debian-cloud/debian-9"
        }
    }

    network_interface {
        subnetwork = var.instance_subnetwork
        access_config {
            # Allocate a one-to-one NAT IP to the instance
        }
    }
  
}
