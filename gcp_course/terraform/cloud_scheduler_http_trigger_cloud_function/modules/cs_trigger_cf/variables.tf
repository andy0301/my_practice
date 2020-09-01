variable "project_id" {
  type = "string"
}

variable "region" {
  type = "string"
}

variable "bucket_name" {
  type = "string"
}

variable "available_memory_mb" {
  type = "string"
}

variable "host" {
  type = "string"
}

variable "nodes" {
  type = "string"
}

variable "max_instances" {
  default = 0
  type    = "string"
}

variable "source_archive_bucket" {
  type = "string"
}

variable "source_archive_object" {
  type = "string"
}

variable "timeout" {
  default = 60
  type    = "string"
}
