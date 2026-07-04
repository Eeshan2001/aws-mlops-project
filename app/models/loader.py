import os
import joblib

from app.exception import ModelLoadException


class ModelLoader:

    def __init__(self):

        self.path = "artifacts"

    def _load(self, filename):

        file_path = os.path.join(
            self.path,
            filename
        )

        if not os.path.exists(file_path):

            raise ModelLoadException(
                f"{filename} not found."
            )

        return joblib.load(file_path)

    def load(self):

        vectorizer = self._load("vectorizer.pkl")

        model = self._load("lda_model.pkl")

        labels = self._load("topic_labels.pkl")

        return vectorizer, model, labels