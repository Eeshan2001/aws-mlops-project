import os

from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import LatentDirichletAllocation

from training.preprocess import clean_text
from training.utils import save_object


ARTIFACT_DIR = "artifacts"

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


if __name__ == "__main__":
    train()