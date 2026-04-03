from pydantic import BaseModel, Field

class CreateDraftSchema(BaseModel):
    to: str = Field(description="Recipient email address,must be a plain string email, NOT a list/array.")
    subject: str = Field(description="Email subject.")
    body: str = Field(description="Email body content.")


class SendDraftSchema(BaseModel):
    draft_id: str = Field(description="The ID of the draft to send.")
