terraform {
  backend "s3" {
    bucket = "andy-aws-example1-terraform-state"
    key    = "global/s3/terraform.tfstate"
    region = "us-west-1"

    dynamodb_table = "andy-aws-example1-terraform-state-locks"
    encrypt        = true
  }
}