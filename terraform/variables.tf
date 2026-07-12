variable "aws_region" {

  default = "us-east-1"

}

variable "project_name" {

  default = "topic-modeling"

}

variable "environment" {

  default = "dev"

}

variable "image_tag" {

  default = "v1"

}

variable "github_owner" {
  default = "Eeshan2001"
}

variable "github_repo" {
  default = "aws-mlops-project"
}

variable "github_branch" {

  default = "master"

}

variable "codestar_connection_arn" {
  default = "arn:aws:codeconnections:us-east-1:123515105191:connection/debac894-1039-409d-87dd-c2a6a7bb5368"
}