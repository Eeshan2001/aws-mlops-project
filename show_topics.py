from training.utils import load_object

vectorizer = load_object(
    "artifacts/vectorizer.pkl"
)

lda = load_object(
    "artifacts/lda_model.pkl"
)

feature_names = vectorizer.get_feature_names_out()

for idx, topic in enumerate(lda.components_):

    top_words = [
        feature_names[i]
        for i in topic.argsort()[-10:]
    ]

    print()

    print(
        f"Topic {idx}:"
    )

    print(
        ", ".join(top_words)
    )