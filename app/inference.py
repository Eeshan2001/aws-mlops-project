import os

from training.utils import load_object
from training.preprocess import clean_text


class TopicPredictor:
    """
    Loads ML artifacts once and performs inference.
    """

    def __init__(self):

        artifact_path = "artifacts"

        self.vectorizer = load_object(
            os.path.join(
                artifact_path,
                "vectorizer.pkl"
            )
        )

        self.model = load_object(
            os.path.join(
                artifact_path,
                "lda_model.pkl"
            )
        )

        self.topic_labels = load_object(
            os.path.join(
                artifact_path,
                "topic_labels.pkl"
            )
        )

    def predict(self, text):

        cleaned = clean_text(text)

        X = self.vectorizer.transform(
            [cleaned]
        )

        probabilities = self.model.transform(X)

        topic_index = probabilities.argmax()

        # Works for both list and dict
        if isinstance(self.topic_labels, dict):
            topic_name = self.topic_labels[topic_index]
        else:
            topic_name = self.topic_labels[topic_index]

        confidence = float(
            probabilities.max()
        )

        return {
            "topic": topic_name,
            "topic_index": int(topic_index),
            "confidence": round(confidence, 4)
        }


predictor = TopicPredictor()