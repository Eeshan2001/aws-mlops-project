from training.utils import load_object

vectorizer = load_object(
    "artifacts/vectorizer.pkl"
)

lda = load_object(
    "artifacts/lda_model.pkl"
)

labels = load_object(
    "artifacts/topic_labels.pkl"
)

text = """
Artificial Intelligence and Machine Learning
are transforming healthcare and robotics.
"""

X = vectorizer.transform([text])

topic_scores = lda.transform(X)

topic_idx = topic_scores.argmax()

print(
    labels[topic_idx]
)