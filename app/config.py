import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = "Topic Modeling"

    APP_VERSION = "1.0"

    DEBUG = True

    HOST = "0.0.0.0"

    PORT = int(
        os.getenv(
            "PORT",
            5000
        )
    )

    AWS_REGION = os.getenv(
        "AWS_REGION",
        "us-east-1"
    )

    MODEL_SOURCE = os.getenv(
        "MODEL_SOURCE",
        "local"
    )

    S3_BUCKET = os.getenv(
        "S3_BUCKET_NAME"
    )