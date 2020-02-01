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

resource "aws_security_group" "instance" {
  name = "inst-001-instance"

  ingress {
    from_port   = var.server_port
    to_port     = var.server_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "andy_instance_001" {
  #ami = "ami-0614811e15abdd2ae"
  ami                    = data.aws_ami.ubuntu-bionic.id
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.instance.id]

  user_data = <<-EOF
                #!/bin/bash
                echo -e "Hello, Taylor!<br>" > index.html
                echo -e "How are you today?<br>" >> index.html
                nohup busybox httpd -f -p ${var.server_port} &
                EOF

  tags = {
    Name = "inst-001"
  }
}