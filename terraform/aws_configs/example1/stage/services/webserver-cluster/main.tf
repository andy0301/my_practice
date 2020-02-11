###################
# Create web server cluster
# By Andy Cai
###################

provider "aws" {
  region = var.region
}

module "aws_example_terraform_module" {
  source = "github.com/andy0301/aws_example_terraform_modules.git//services/webservers-cluster?ref=v1.2"

   # module config for all variables
  cluster_name = "webservers-stage"
  db_remote_state_bucket = "andy-aws-example1-terraform-state"
  db_remote_state_key = "stage/data-stores/mysql/terraform.tfstate"
  region = var.region
  server_port = var.server_port
  vm_type = "t2.micro"
  autoscale_min_size = 2
  autoscale_max_size = 2
}