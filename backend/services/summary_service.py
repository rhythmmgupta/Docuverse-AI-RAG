# backend/services/summary_service.py

def build_summary_prompt(context):

    return f"""
Generate a professional summary.

Format:

Executive Summary

Key Points

Important Dates

Risks

Action Items

Document:

{context}
"""