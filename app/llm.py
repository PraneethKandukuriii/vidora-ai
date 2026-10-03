import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def create_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0,
    )


def generate_answer(context: str, question: str) -> str:
    llm = create_llm()

    prompt = f"""
You are a helpful AI assistant answering questions about a YouTube video.

Use only the context provided below to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
If the answer cannot be found in the context, say:
"I couldn't find the answer in the video."
"""

    response = llm.invoke(prompt)

    return response.text


if __name__ == "__main__":
    context = """
    Machine learning allows computers to learn patterns from data.
    Neural networks are commonly used in deep learning.
    """

    question = "What is machine learning?"

    answer = generate_answer(
        context=context,
        question=question,
    )

    print("\nAnswer:")
    print(answer)