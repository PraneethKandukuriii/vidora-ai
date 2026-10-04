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


def generate_response(
    user_request: str,
    context: str,
    conversation_history: str = "",
) -> str:
    llm = create_llm()

    prompt = f"""
You are Vidora, an AI assistant that answers questions about a YouTube video.

Answer the user's request directly using the provided video context.

Response rules:

1. Understand what the user is actually asking.
2. Give the direct answer first.
3. Match the response length to the question.
4. Use short paragraphs for explanations.
5. Use bullet points when listing multiple ideas.
6. Use examples when they make the explanation clearer.
7. Do not repeat information unnecessarily.
8. Do not invent information that isn't supported by the video.
9. If the video context does not contain the answer, clearly say:
   "I couldn't find the answer in the video."
10. If the user asks a follow-up question, use the conversation history
    to understand what they are referring to.

Conversation history:
{conversation_history}

Video context:
{context}

User request:
{user_request}
"""

    response = llm.invoke(prompt)

    return response.text


if __name__ == "__main__":
    context = """
    Machine learning allows computers to learn patterns from data.
    Neural networks are commonly used in deep learning.
    """

    user_request = "What is machine learning?"

    response = generate_response(
        user_request=user_request,
        context=context,
    )

    print("\nResponse:")
    print(response)