try:
    from .llm import generate_answer
except ImportError:  # pragma: no cover - direct script execution
    from llm import generate_answer


def generate_summary(transcript: str) -> str:
    prompt = f"""
You are Vidora, an AI assistant that summarizes YouTube videos.

Summarize the following transcript clearly and accurately.

Transcript:
{transcript}

Follow these rules:
- Start with a short 2-3 sentence overview.
- Then provide the main points as 4-7 bullet points.
- Focus on the most important ideas.
- Use simple and natural language.
- Do not invent information.
- Do not unnecessarily repeat the transcript.
"""

    return generate_answer(
        context=prompt,
        question="Summarize the video.",
    )


if __name__ == "__main__":
    transcript = """
    Machine learning allows computers to learn from data.
    Neural networks are commonly used in deep learning.
    Python is widely used for artificial intelligence.
    """

    summary = generate_summary(transcript)

    print("\nSummary:")
    print(summary)