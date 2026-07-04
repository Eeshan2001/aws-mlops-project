class TopicModelException(Exception):
    """Custom exception for the application."""

    def __init__(self, message):
        super().__init__(message)