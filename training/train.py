import json
import os
import shutil
from datetime import datetime, UTC

from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import LatentDirichletAllocation

from training.preprocess import clean_text
from training.utils import save_object


ARTIFACT_DIR = "artifacts"

VERSION = "1.0.0"

N_TOPICS = 10


def train():

    print("Loading dataset...")

    dataset = fetch_20newsgroups(
        subset="train",
        remove=("headers", "footers", "quotes")
    )

    documents = dataset.data

    print(f"Documents Loaded: {len(documents)}")

    print("Cleaning text...")

    cleaned_docs = [
        clean_text(doc)
        for doc in documents
    ]

    print("Creating Bag Of Words...")

    vectorizer = CountVectorizer(
        max_df=0.95,
        min_df=2,
        stop_words="english"
    )

    X = vectorizer.fit_transform(
        cleaned_docs
    )

    print("Training LDA Model...")

    lda = LatentDirichletAllocation(
        n_components=N_TOPICS,
        random_state=42,
        learning_method="batch"
    )

    lda.fit(X)

    print("Saving Artifacts...")

    save_object(
        os.path.join(
            ARTIFACT_DIR,
            "vectorizer.pkl"
        ),
        vectorizer
    )

    save_object(
        os.path.join(
            ARTIFACT_DIR,
            "lda_model.pkl"
        ),
        lda
    )

    # Replace these labels after inspecting the output of show_topics.py
    topic_labels = {
        0: "Cryptography & Security",
        1: "Space Exploration",
        2: "Automobiles",
        3: "Healthcare & Medicine",
        4: "Sports (Hockey)",
        5: "Religion",
        6: "Software & Operating Systems",
        7: "Computer Hardware",
        8: "Politics & International Affairs",
        9: "Gun Laws & Politics"
    }

    save_object(
        os.path.join(
            ARTIFACT_DIR,
            "topic_labels.pkl"
        ),
        topic_labels
    )

    print("Training Completed")

    metadata = {
        "model_name": "LDA Topic Model",
        "model_version": "1.0.0",
        "training_date": datetime.now(UTC).isoformat(),
        "n_topics": N_TOPICS,
        "vectorizer": "CountVectorizer",
        "dataset": "20 Newsgroups"
    }

    with open("artifacts/model_metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    artifacts = [
        "lda_model.pkl",
        "vectorizer.pkl",
        "topic_labels.pkl",
        "model_metadata.json"
    ]

    for artifact in artifacts:
        source = os.path.join("artifacts", artifact)

        filename, extension = os.path.splitext(artifact)

        destination = os.path.join(
            "artifacts",
            f"{filename}_{VERSION}{extension}"
        )

        shutil.copy(source, destination)

    print(f"Versioned artifacts created for version {VERSION}")

if __name__ == "__main__":
    train()