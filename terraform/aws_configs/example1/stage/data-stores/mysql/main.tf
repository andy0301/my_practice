###################
# create mysql db as backend data store
# By Andy Cai
###################

provider "aws" {
    region = var.region
}

module "aws_example_terraform_module" {
  source = "github.com/andy0301/aws_example_terraform_modules.git//data-store/db?ref=v1.3"

  db_cluster_name = "andy-aws-example"
  db_engine = "mysql"
  db_storage_size = 10
  db_instance_type = "db.t2.micro"
  db_name = "andy_example1_db"
  db_admin_username = "admin"
  db_password = var.db_password
}