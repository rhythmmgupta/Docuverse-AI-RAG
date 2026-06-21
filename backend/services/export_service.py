from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def create_report(
    filename,
    document_name,
    summary,
    insights,
    history
):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "DocuVerse AI Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Document: {document_name}",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            summary if summary else "No summary available.",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Insights",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            insights if insights else "No insights available.",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    content.append(
        Paragraph(
            "Chat History",
            styles["Heading1"]
        )
    )

    if history:

        for item in history:

            content.append(
                Paragraph(
                    f"<b>Question:</b> {item.get('question', '')}",
                    styles["BodyText"]
                )
            )

            content.append(
                Paragraph(
                    f"<b>Answer:</b> {item.get('answer', '')}",
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 10)
            )

    else:

        content.append(
            Paragraph(
                "No chat history available.",
                styles["BodyText"]
            )
        )

    pdf.build(content)

    return filename