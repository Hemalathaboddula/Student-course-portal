provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = "t3.micro"
  key_name      = var.key_name

  tags = {
    Name = "devops-ec2"
  }
}

output "public_ip" {
  value = aws_instance.web.public_ip
}