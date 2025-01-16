# Генерація випадкового префікса для забезпечення унікальності імені безпекової групи
resource "random_id" "suffix" {
  byte_length = 8
}

# Створення безпекової групи з унікальним ім'ям
resource "aws_security_group" "web_app" {
  name        = "web_app_${random_id.suffix.hex}"  # Унікальне ім'я групи
  description = "Security group for web app"
  vpc_id      = "vpc-083d3020ef74c0d98"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "web_app"
  }
}

