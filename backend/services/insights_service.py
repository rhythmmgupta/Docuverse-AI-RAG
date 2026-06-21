# backend/services/insights_service.py

def build_insights_prompt(context):

    return f"""
Extract:

1. Dates
2. People
3. Organizations
4. Money Values
5. Risks

Document:

{context}
"""