resource "aws_ecs_service" "main" {

  name = "topic-modeling-service"

  cluster = aws_ecs_cluster.main.id

  task_definition = aws_ecs_task_definition.main.arn

  desired_count = 1

  launch_type = "FARGATE"

  network_configuration {

    assign_public_ip = true

    subnets = [

      aws_subnet.public_a.id,

      aws_subnet.public_b.id

    ]

    security_groups = [

      aws_security_group.ecs.id

    ]

  }

  load_balancer {

    target_group_arn = aws_lb_target_group.main.arn

    container_name = var.project_name

    container_port = 5000

  }

  depends_on = [

    aws_lb_listener.http

  ]

}