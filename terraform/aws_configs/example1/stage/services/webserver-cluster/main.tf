provider "aws" {
  region = "us-west-1"
}

data "aws_ami" "ubuntu-bionic" {
  most_recent = true

  filter {
    name   = "name"
    values = ["*ubuntu-1804-lts*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["247102896272"]

}

data "aws_vpc" "default" {
  default = true
}

data "aws_subnet_ids" "default" {
  vpc_id = data.aws_vpc.default.id
}

 # using terraform_remote_state data source to get db outputs
data "terraform_remote_state" "db" {
  backend = "S3"

  config = {
    bucket = "andy-aws-example1-terraform-state"
    key = "stage/data-stores/mysql/terraform.tfstate"
    region = "us-west-1"
  }
}

 # using template_file.xxx.rendered to fetch variables values from user scripts or data
data "template_file" "user_data" {
  template = file("user_data.sh")

  vars = {
    server_port = var.server_port
    db_address = data.terraform_remote_state.db.outputs.address
    db_port = data.terraform_remote_state.db.outputs.port
  }
}

resource "aws_launch_configuration" "andy_asg_example" {
  #ami = "ami-0614811e15abdd2ae"
  image_id        = data.aws_ami.ubuntu-bionic.id
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.instance.id]

  user_data = data.template_file.user_data.rendered

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "andy_asg_example" {
  launch_configuration = aws_launch_configuration.andy_asg_example.name
  vpc_zone_identifier  = data.aws_subnet_ids.default.ids

  target_group_arns = [aws_lb_target_group.asg.arn]
  health_check_type = "ELB"

  min_size = 2
  max_size = 6

  tag {
    key                 = "Name"
    value               = "andy-asg-example"
    propagate_at_launch = true
  }

  lifecycle {
    create_before_destroy = true
  }
}