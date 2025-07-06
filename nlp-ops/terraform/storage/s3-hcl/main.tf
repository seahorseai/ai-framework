# Terraform configuration for AWS
provider "aws" {
  region = "us-east-1" # Change to your preferred region
}

# Create an S3 bucket
resource "aws_s3_bucket" "example" {
  bucket = "my-example-s3-bucket"  # Replace with a unique bucket name
  acl    = "private"

  tags = {
    Name        = "MyExampleBucket"
    Environment = "Development"
  }
}

# Enable versioning for the bucket
resource "aws_s3_bucket_versioning" "example" {
  bucket = aws_s3_bucket.example.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Enable server-side encryption for the bucket
resource "aws_s3_bucket_server_side_encryption_configuration" "example" {
  bucket = aws_s3_bucket.example.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Optional: Bucket policy for public access prevention
resource "aws_s3_bucket_policy" "example" {
  bucket = aws_s3_bucket.example.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "DenyPublicRead"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.example.arn}/*"
        Condition = {
          Bool = {
            "aws:SecureTransport" = "false"
          }
        }
      }
    ]
  })
}
