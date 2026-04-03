from typing import Literal
from pydantic import BaseModel, Field
from typing import Literal, Optional

TriageLabel = Literal[
    "FOLLOW_UP_REQUIRED",
    "READ_LATER",
    "CHECK_LATER",
    "PROMOTIONAL",
    "FYI_NOTIFICATION",
]

class TriageOutput(BaseModel):
    """
    Structured output from the triage agent.
    Classifies an incoming email into a productivity label.
    """

    triage_label: TriageLabel = Field(
        description=(
            "Productivity label assigned to the email. "
            "FOLLOW_UP_REQUIRED = Action or reply needed (High Urgency & Standard Follow-ups), "
            "READ_LATER = Informational only, no action required, "
            "CHECK_LATER = Unknown sender or cold outreach, "
            "PROMOTIONAL = Marketing or sales emails, "
            "FYI_NOTIFICATION = Automated alerts or confirmations."
        )
    )

    requires_reply: bool = Field(
        description="True ONLY when triage_label is FOLLOW_UP_REQUIRED. False for all others."
    )

    triage_notes: Optional[str] = Field(
        default=None,
        description="One concise sentence explaining why this label and priority were chosen."
    )

    priority_score: int = Field(
        ge=1,
        le=5,
        description=(
            "Urgency score: 5 = Critical/Urgent (Reply NOW), "
            "4 = High priority (Reply today), "
            "3 = Standard follow-up (this week), "
            "2 = Low priority read, "
            "1 = Ignore/Archive."
        )
    )