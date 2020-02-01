terraform {
  backend "s3" {
    bucket = "andy-aws-example1-terraform-state"
    key    = "stage/data-stores/mysql/terraform.tfstate"
    region = "us-west-1"

    dynamodb_table = "andy-aws-example1-terraform-state-locks"
    encrypt        = true
  }
}