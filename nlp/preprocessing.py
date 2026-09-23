import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocessing(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))

    words = [word for word in words if word not in stop_words]

    return words


def clean_text(text):
    words = preprocessing(text)
    return " ".join(words)