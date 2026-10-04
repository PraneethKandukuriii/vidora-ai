def detect_intent(question: str) -> str:
    question = question.lower().strip()

    if any(
        phrase in question
        for phrase in [
            "transcript",
            "full transcript",
            "whole transcript",
        ]
    ):
        return "transcript"

    if any(
        phrase in question
        for phrase in [
            "summarize",
            "summary",
            "summarise",
            "give me a summary",
        ]
    ):
        return "summary"

    if any(
        phrase in question
        for phrase in [
            "thanks",
            "thank you",
            "okay",
            "ok",
            "accha",
            "cool",
        ]
    ):
        return "casual"

    return "question"