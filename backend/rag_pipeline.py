def answer_question(query, retriever, llm):
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer ONLY from the context below.
    If not found, say "Not found in document".

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    messages = [{"role": "user", "content": prompt}]
    response = llm.chat_completion(
        messages=messages,
        max_tokens=200
    )

    return response.choices[0].message.content