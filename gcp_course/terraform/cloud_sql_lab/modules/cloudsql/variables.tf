variable "database_version" {
  description = "Database Version, default is MYSQL_5_6"
  type        = string
  default     = "MYSQL_5_6"
}

variable "region" {
  description = "Region name"
  type        = string
  default     = "us-central1"
}

variable "tier" {
  description = "Database instance tier, default is db-f1-micro"
  type        = string
  default     = "db-f1-micro"
}

variable "disk_size" {
  description = "DB instance disk size, default is 10G"
  type        = number
  default     = 10
}

variable "sql_user_name" {
  description = "SQL instance user name"
  type        = string
  default     = ""
}

variable "sql_user_password" {
  description = "SQL instance user password"
  type        = string
  default     = ""
}

