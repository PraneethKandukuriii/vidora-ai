def rewrite_query(
    question: str,
    chat_history: list[tuple[str, str]],
) -> str:

    question = question.strip()

    if not chat_history:
        return question

    question_lower = question.lower()

    follow_up_indicators = [
        "it",
        "this",
        "that",
        "they",
        "them",
        "he",
        "she",
        "these",
        "those",
        "why",
        "how",
        "what about",
        "and what",
        "also",
    ]

    is_follow_up = any(
        indicator in question_lower
        for indicator in follow_up_indicators
    )

    if not is_follow_up:
        return question

    previous_question, _ = chat_history[-1]

    return f"{previous_question} {question}"