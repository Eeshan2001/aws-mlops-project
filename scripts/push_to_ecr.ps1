$AccountId = aws sts get-caller-identity --query Account --output text
$Region = "us-east-1"
$Repository = "topic-modeling-repo"
$Image = "topic-modeling-app"
$Tag = "v1"

docker build -t "${Image}:$Tag" .

aws ecr get-login-password --region $Region |
docker login --username AWS --password-stdin "$AccountId.dkr.ecr.$Region.amazonaws.com"

docker tag "${Image}:$Tag" `
"${AccountId}.dkr.ecr.${Region}.amazonaws.com/${Repository}:${Tag}"

docker push "${AccountId}.dkr.ecr.${Region}.amazonaws.com/${Repository}:${Tag}"