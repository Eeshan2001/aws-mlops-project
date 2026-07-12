resource "aws_ecs_task_definition" "main" {

  family = "${var.project_name}-task"

  network_mode = "awsvpc"

  requires_compatibilities = [
    "FARGATE"
  ]

  cpu = 256

  memory = 512

  execution_role_arn = aws_iam_role.ecs_execution_role.arn

  container_definitions = jsonencode([

    {

      name = var.project_name

      image = "${aws_ecr_repository.main.repository_url}:latest"

      essential = true

      portMappings = [

        {

          containerPort = 5000

          protocol = "tcp"

        }

      ]

      logConfiguration = {

        logDriver = "awslogs"

        options = {

          awslogs-group = aws_cloudwatch_log_group.ecs.name

          awslogs-region = var.aws_region

          awslogs-stream-prefix = "ecs"

        }

      }

    }

  ])

}