variable "server_port" {
  description = "The port the server will use for HTTP requests"
  type        = number
  default     = 8080
}

variable "region" {
  description = "Region which the cluster will be built"
  type = string
}