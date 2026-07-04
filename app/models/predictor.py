import numpy as np

from training.preprocess import clean_text

from app.models.loader import ModelLoader


class TopicPredictor:

    def __init__(self):

        loader = ModelLoader()

        (
            self.vectorizer,
            self.model,
            self.labels
        ) = loader.load()

    def predict(self, text):

        cleaned = clean_text(text)

        X = self.vectorizer.transform(
            [cleaned]
        )

        probabilities = self.model.transform(X)

        topic = int(
            np.argmax(probabilities)
        )

        confidence = float(
            probabilities.max()
        )

        return {

            "topic": self.labels[topic],

            "topic_index": topic,

            "confidence": round(
                confidence,
                4
            )

        }