# backend/services/compare_service.py

def build_compare_prompt(doc1, doc2):

    return f"""
Compare both documents.

Document A:

{doc1}

Document B:

{doc2}

Provide:

Differences
Missing Clauses
Risks
Recommendations
"""