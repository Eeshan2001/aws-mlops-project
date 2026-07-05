resource "aws_cloudwatch_log_group" "ecs" {

  name = "/ecs/topic-modeling"

  retention_in_days = 14

}