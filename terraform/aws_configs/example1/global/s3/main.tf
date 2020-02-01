###################
# create S3 bucket to store terraform.tfstate
# by Andy Cai
###################

resource "aws_s3_bucket" "terraform_state" {
  bucket = "andy-aws-example1-terraform-state"

  # Prevent accidental deletion of this S3 bucket
  lifecycle {
    prevent_destroy = true
  }

  # Enable versioning of state files
  versioning {
    enabled = true
  }

  # Enable server-side encryption by default
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}

# using dynamodb table for locking state file when concurrently modify
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "andy-aws-example1-terraform-state-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}