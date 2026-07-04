class TopicModelException(Exception):
    """
    Base exception for Topic Modeling application.
    """

    def __init__(self, message):

        super().__init__(message)


class ValidationException(TopicModelException):
    """
    Raised for invalid user input.
    """

    pass


class ModelLoadException(TopicModelException):
    """
    Raised when model artifacts cannot be loaded.
    """

    pass


class PredictionException(TopicModelException):
    """
    Raised during prediction failures.
    """

    pass