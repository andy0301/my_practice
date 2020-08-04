variable "project_id" {
  type = string
}

variable "service_name" {
  type = string
}

variable "region" {
  default = "us-central1"
  type    = string
}

variable "zone" {
  type = string
}

variable "node_count" {
  type = string
}

variable "machine_type" {
  type = string
}

variable "disk_size_gb" {
  type    = number
  default = 100
}
