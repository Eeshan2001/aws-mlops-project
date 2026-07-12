resource "aws_iam_role" "codepipeline_role" {

  name = "${var.project_name}-codepipeline-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Principal = {

          Service = "codepipeline.amazonaws.com"

        }

        Action = "sts:AssumeRole"

      }

    ]

  })

}

resource "aws_iam_role_policy_attachment" "pipeline" {

  role = aws_iam_role.codepipeline_role.name

  policy_arn = "arn:aws:iam::aws:policy/AWSCodePipeline_FullAccess"

}

resource "aws_codepipeline" "main" {

  name = "${var.project_name}-pipeline"

  role_arn = aws_iam_role.codepipeline_role.arn

  artifact_store {

    location = aws_s3_bucket.pipeline_artifacts.bucket

    type = "S3"
  }

  stage {

    name = "Source"

    action {

      name = "Source"

      category = "Source"

      owner = "AWS"

      provider = "CodeStarSourceConnection"

      version = "1"

      output_artifacts = ["source_output"]

      configuration = {
        ConnectionArn    = var.codestar_connection_arn
        FullRepositoryId = "${var.github_owner}/${var.github_repo}"
        BranchName       = var.github_branch
      }
    }
  }

  stage {

    name = "Build"

    action {

      name = "Build"

      category = "Build"

      owner = "AWS"

      provider = "CodeBuild"

      input_artifacts = ["source_output"]

      output_artifacts = ["build_output"]

      version = "1"

      configuration = {
        ProjectName = aws_codebuild_project.main.name
      }
    }
  }

  stage {

    name = "Deploy"

    action {

      name = "Deploy"

      category = "Deploy"

      owner = "AWS"

      provider = "ECS"

      version = "1"

      input_artifacts = ["build_output"]

      configuration = {
        ClusterName = aws_ecs_cluster.main.name
        ServiceName = aws_ecs_service.main.name
        FileName    = "imagedefinitions.json"
      }
    }
  }
}