#!/bin/bash

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

REGION="us-east-1"

REPOSITORY="topic-modeling-repo"

IMAGE="topic-modeling-app"

TAG="v1"

docker build -t ${IMAGE}:${TAG} .

aws ecr get-login-password --region ${REGION} | \
docker login --username AWS \
--password-stdin ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

docker tag ${IMAGE}:${TAG} \
${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY}:${TAG}

docker push \
${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY}:${TAG}