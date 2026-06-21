def build_followup_prompt(
    question,
    answer
):
    return f"""
Generate 3 follow-up questions.

Question:
{question}

Answer:
{answer}

Only return questions.
"""