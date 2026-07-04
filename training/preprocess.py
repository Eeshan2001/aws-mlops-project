import re
import string

from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words("english"))


def clean_text(text: str) -> str:
    """
    Clean incoming text.
    """

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"\d+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = text.split()

    words = [
        word
        for word in words
        if word not in STOP_WORDS
    ]

    return " ".join(words)