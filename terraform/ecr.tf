resource "aws_ecr_repository" "topic_model_repo" {

  name = "${var.project_name}-repo"

  image_tag_mutability = "MUTABLE"

  force_delete = true

  image_scanning_configuration {

    scan_on_push = true

  }

  encryption_configuration {

    encryption_type = "AES256"

  }

  tags = {

    Project = var.project_name

    Environment = var.environment

  }

}