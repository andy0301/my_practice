###################
# create mysql db as backend data store
# By Andy Cai
###################

provider "aws" {
    region = "us-west-1"
}

resource "aws_db_instance" "mysql_example" {
  identifier_prefix = "andy-aws-example1"
  engine = "mysql"
  allocated_storage = 10
  instance_class = "db.t2.micro"
  name = "andy_example1_db"
  username = "admin"

  password = var.db_password
}