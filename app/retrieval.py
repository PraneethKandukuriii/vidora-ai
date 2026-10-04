from langchain_core.documents import Document


def determine_retrieval_depth(question: str) -> int:
    question = question.lower().strip()

    complex_indicators = [
        "explain",
        "why",
        "how",
        "compare",
        "difference",
        "relationship",
        "advantages",
        "disadvantages",
        "detailed",
        "multiple",
    ]

    if any(
        indicator in question
        for indicator in complex_indicators
    ):
        return 6

    return 3


def adaptive_search(
    vector_store,
    query: str,
    initial_k: int = 3,
    expanded_k: int = 6,
    score_threshold: float = 0.8,
) -> list[Document]:

    initial_results = vector_store.similarity_search_with_score(
        query,
        k=initial_k,
    )

    if not initial_results:
        print("\nRetrieval: no results found.")
        return []

    best_score = initial_results[0][1]

    print("\nRetrieval diagnostics:")
    print(f"Initial results: {len(initial_results)}")
    print(f"Best score: {best_score:.4f}")

    if best_score <= score_threshold:
        print("Decision: strong match")
        print("Using initial results.")

        return [
            document
            for document, _ in initial_results
        ]

    print("Decision: weak match")
    print("Expanding retrieval.")

    expanded_results = vector_store.similarity_search_with_score(
        query,
        k=expanded_k,
    )

    print(f"Expanded results: {len(expanded_results)}")

    return [
        document
        for document, _ in expanded_results
    ]