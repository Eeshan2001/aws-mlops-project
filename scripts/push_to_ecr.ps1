# ===============================
# Configuration
# ===============================

$Region = "us-east-1"
$AccountId = "123515105191"

$RepositoryName = "topic-modeling-repo"
$ImageName = "topic-modeling-app"

$VersionTag = "v1"
$LatestTag = "latest"

$RepositoryUri = "$AccountId.dkr.ecr.$Region.amazonaws.com/$RepositoryName"

# ===============================
# Login to Amazon ECR
# ===============================

Write-Host ""
Write-Host "========== Logging into Amazon ECR ==========" -ForegroundColor Cyan

$auth = aws ecr get-authorization-token `
    --region $Region `
    --query "authorizationData[0].authorizationToken" `
    --output text

$decoded = [System.Text.Encoding]::UTF8.GetString(
    [System.Convert]::FromBase64String($auth)
)

$user, $pass = $decoded.Split(":",2)

docker login `
    --username $user `
    --password $pass `
    "$AccountId.dkr.ecr.$Region.amazonaws.com"

if ($LASTEXITCODE -ne 0) {
    Write-Host "ECR Login Failed!" -ForegroundColor Red
    exit 1
}

# ===============================
# Build Docker Image
# ===============================

Write-Host ""
Write-Host "========== Building Docker Image ==========" -ForegroundColor Cyan

docker build -t "${ImageName}:${VersionTag}" .

if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker Build Failed!" -ForegroundColor Red
    exit 1
}

# ===============================
# Tag Images
# ===============================

Write-Host ""
Write-Host "========== Tagging Images ==========" -ForegroundColor Cyan

docker tag "${ImageName}:${VersionTag}" "${RepositoryUri}:${VersionTag}"
docker tag "${ImageName}:${VersionTag}" "${RepositoryUri}:${LatestTag}"

# ===============================
# Push Version Tag
# ===============================

Write-Host ""
Write-Host "========== Pushing v1 ==========" -ForegroundColor Cyan

docker push "${RepositoryUri}:${VersionTag}"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Push Failed!" -ForegroundColor Red
    exit 1
}

# ===============================
# Push Latest Tag
# ===============================

Write-Host ""
Write-Host "========== Pushing latest ==========" -ForegroundColor Cyan

docker push "${RepositoryUri}:${LatestTag}"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Push Failed!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host " Docker image pushed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "v1     -> ${RepositoryUri}:${VersionTag}"
Write-Host "latest -> ${RepositoryUri}:${LatestTag}"
Write-Host "==========================================" -ForegroundColor Green