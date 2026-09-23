from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nlp.preprocessing import clean_text


TOPICS = {

    "variables": [
        "python variables",
        "creating variables",
        "assigning values",
        "variable declaration",
        "store value in variable",
        "data types variables"
    ],

    "conditions": [
        "python if statement",
        "if else",
        "elif condition",
        "conditional statements",
        "python conditions",
        "decision making"
    ],

    "loops": [
        "python loops",
        "for loop",
        "while loop",
        "nested loops",
        "loop iteration",
        "repeat code"
    ],

    "functions": [
        "python functions",
        "def function",
        "function parameters",
        "return statement",
        "calling functions",
        "function arguments"
    ]

}


def detect_topic(text):

    cleaned_text = clean_text(text)

    if not cleaned_text:
        return {
            "topic": "unknown",
            "confidence": 0
        }


    topic_names = list(TOPICS.keys())


    documents = []

    labels = []


    for topic, examples in TOPICS.items():

        for example in examples:

            documents.append(
                clean_text(example)
            )

            labels.append(topic)


    documents.append(cleaned_text)


    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(
        documents
    )


    similarities = cosine_similarity(
        matrix[-1],
        matrix[:-1]
    )[0]


    best_index = similarities.argmax()

    best_score = similarities[best_index]


    if best_score < 0.10:

        return {
            "topic": "unknown",
            "confidence": round(
                float(best_score) * 100,
                2
            )
        }


    return {
        "topic": labels[best_index],
        "confidence": round(
            float(best_score) * 100,
            2
        )
    }
