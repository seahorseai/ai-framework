# main.tf

# Specify the provider
provider "aws" {
  region = "eu-west-3" # Set your desired AWS region
}

# VPC
resource "aws_vpc" "example_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "example-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "example_igw" {
  vpc_id = aws_vpc.example_vpc.id

  tags = {
    Name = "example-igw"
  }
}

# Public Subnets
resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.example_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "eu-west-3a"

  tags = {
    Name = "example-public-subnet-1"
  }
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id                  = aws_vpc.example_vpc.id
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "eu-west-3b"

  tags = {
    Name = "example-public-subnet-2"
  }
}

# Private Subnets
resource "aws_subnet" "private_subnet_1" {
  vpc_id            = aws_vpc.example_vpc.id
  cidr_block        = "10.0.3.0/24"
  availability_zone = "eu-west-3a"

  tags = {
    Name = "example-private-subnet-1"
  }
}

resource "aws_subnet" "private_subnet_2" {
  vpc_id            = aws_vpc.example_vpc.id
  cidr_block        = "10.0.4.0/24"
  availability_zone = "eu-west-3b"

  tags = {
    Name = "example-private-subnet-2"
  }
}

# Public Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.example_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.example_igw.id
  }

  tags = {
    Name = "example-public-rt"
  }
}

# Associate Public Route Table with Public Subnets
resource "aws_route_table_association" "public_rt_assoc_1" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_rt_assoc_2" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_rt.id
}

# Elastic IP for NAT Gateway
resource "aws_eip" "nat_eip" {
  domain = "vpc"
}

# NAT Gateway
resource "aws_nat_gateway" "nat_gw" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public_subnet_1.id

  tags = {
    Name = "example-nat-gw"
  }
}

# Private Route Table
resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.example_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gw.id
  }

  tags = {
    Name = "example-private-rt"
  }
}

# Associate Private Route Table with Private Subnets
resource "aws_route_table_association" "private_rt_assoc_1" {
  subnet_id      = aws_subnet.private_subnet_1.id
  route_table_id = aws_route_table.private_rt.id
}

resource "aws_route_table_association" "private_rt_assoc_2" {
  subnet_id      = aws_subnet.private_subnet_2.id
  route_table_id = aws_route_table.private_rt.id
}
