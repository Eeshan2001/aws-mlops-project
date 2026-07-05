output "vpc_id" {

  value = aws_vpc.main.id

}

output "public_subnets" {

  value = [

    aws_subnet.public_a.id,

    aws_subnet.public_b.id

  ]

}

output "repository_url" {

  value = aws_ecr_repository.main.repository_url

}

output "cluster_name" {

  value = aws_ecs_cluster.main.name

}

output "ecs_execution_role_arn" {

  value = aws_iam_role.ecs_execution_role.arn

}

output "alb_security_group_id" {

  value = aws_security_group.alb.id

}

output "ecs_security_group_id" {

  value = aws_security_group.ecs.id

}