provider "aws" {
  region = "ap-south-1"
}

# ✅ Security Group
resource "aws_security_group" "web_sg" {
  name = "learnhub-sg"

  # SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP (nginx)
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Django (optional)
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ✅ EC2 Instance
resource "aws_instance" "app_server" {
  ami           = "ami-0e12ffc2dd465f6e4"   # ✅ Works for your account (you can change later)
  instance_type = "t3.micro"               # ✅ works for you (since script worked)
  key_name      = "app-key"                # ✅ your new key

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "LearnHubServer"
  }
}

# ✅ Output Public IP
output "public_ip" {
  value = aws_instance.app_server.public_ip
}