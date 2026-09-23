from nlp.topic_detector import detect_topic


WEAKNESS_KEYWORDS = {

    "variables": [
        "confused",
        "dont understand",
        "not understand",
        "difficult",
        "confusing",
        "struggling",
        "weak"
    ],

    "conditions": [
        "confused",
        "dont understand",
        "not understand",
        "difficult",
        "confusing",
        "struggling",
        "weak"
    ],

    "loops": [
        "confused",
        "dont understand",
        "not understand",
        "difficult",
        "confusing",
        "struggling",
        "weak"
    ],

    "functions": [
        "confused",
        "dont understand",
        "not understand",
        "difficult",
        "confusing",
        "struggling",
        "weak"
    ]

}


def detect_knowledge_gap(text):

    analysis = detect_topic(text)

    topic = analysis["topic"]

    confidence = analysis["confidence"]


    if topic == "unknown":

        return {
            "gap_detected": False,
            "topic": "unknown",
            "confidence": confidence,
            "message": "Could not identify a learning topic."
        }


    text_lower = text.lower()


    weakness_found = False


    for keyword in WEAKNESS_KEYWORDS.get(
        topic,
        []
    ):

        if keyword in text_lower:

            weakness_found = True

            break


    if weakness_found:

        return {
            "gap_detected": True,
            "topic": topic,
            "confidence": confidence,
            "message":
                f"Knowledge gap detected in {topic}.",
            "side_quest":
                f"Practice {topic} with a personalized side quest."
        }


    return {
        "gap_detected": False,
        "topic": topic,
        "confidence": confidence,
        "message":
            f"You seem comfortable with {topic}.",
        "side_quest": None
    }
