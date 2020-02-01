variable "server_port" {
  description = "The port the server will use for HTTP requests"
  type        = number
  default     = 8080
}

variable "alb_port" {
  description = "The port the Application Loadbalancer for HTTP requests"
  type        = number
  default     = 80
}
