variable "db_password" {
  type        = string
  description = "Just for example so input password from environment variable"
  # you will need set TF_VAR_db_password="xxx"
}

variable "region" {
  description = "The region name"
  type = string
}