resource "aws_iam_role" "codebuild" {

  name = "${var.project_name}-codebuild-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Principal = {

          Service = "codebuild.amazonaws.com"

        }

        Action = "sts:AssumeRole"

      }

    ]

  })

}

resource "aws_iam_role_policy_attachment" "ecr_power" {

  role = aws_iam_role.codebuild.name

  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPowerUser"

}

resource "aws_iam_role_policy_attachment" "logs" {

  role = aws_iam_role.codebuild.name

  policy_arn = "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"

}

resource "aws_iam_role_policy" "artifact_bucket" {

  role = aws_iam_role.codebuild.id

  policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Action = [

          "s3:GetObject",

          "s3:PutObject",

          "s3:ListBucket"

        ]

        Resource = [

          aws_s3_bucket.pipeline_artifacts.arn,

          "${aws_s3_bucket.pipeline_artifacts.arn}/*"

        ]

      }

    ]

  })

}

resource "aws_codebuild_project" "main" {

  name         = "${var.project_name}-build"
  service_role = aws_iam_role.codebuild.arn

  artifacts {
    type = "CODEPIPELINE"
  }

  environment {

    compute_type = "BUILD_GENERAL1_SMALL"

    image = "aws/codebuild/standard:7.0"

    type = "LINUX_CONTAINER"

    privileged_mode = true
  }

  source {

    type = "CODEPIPELINE"

    buildspec = "buildspec.yml"

  }

  logs_config {

    cloudwatch_logs {

      group_name = "/codebuild/${var.project_name}"

      stream_name = "build"

    }

  }

}