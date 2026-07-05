output "cluster_name" {

  value = aws_ecs_cluster.main.name

}

output "ecs_execution_role_arn" {

  value = aws_iam_role.ecs_execution_role.arn

}

output "alb_security_group" {

  value = aws_security_group.alb.id

}

output "ecs_security_group" {

  value = aws_security_group.ecs.id

}