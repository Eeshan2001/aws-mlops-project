data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "pipeline_artifacts" {

  bucket = "${var.project_name}-pipeline-artifacts-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name        = "CodePipeline Artifacts"
    Environment = "dev"
    Project     = var.project_name
  }
}

resource "aws_s3_bucket_versioning" "pipeline_artifacts" {

  bucket = aws_s3_bucket.pipeline_artifacts.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "pipeline_artifacts" {

  bucket = aws_s3_bucket.pipeline_artifacts.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}