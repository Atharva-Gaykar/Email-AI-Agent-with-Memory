from app.database.models import User, ReceivedEmail, SentEmail
from sqlalchemy.orm import Session

def get_or_create_user(session, email: str):
    user = session.query(User).filter_by(email=email).first()

    if not user:
        user = User(email=email)
        session.add(user)
        session.commit()
        session.refresh(user)

    return user




def save_received_email(session: Session, owner_id: int,thread_id: str, state: dict) -> ReceivedEmail:
    """
    Persists the incoming email and the agent's initial triage results.
    """
    email = ReceivedEmail(
        owner_id       = owner_id,
        thread_id      = thread_id,
        sender_email   = state.get("sender_email_id"),
        subject        = state.get("sender_subject"),
        body           = state.get("sender_email_body"),
        is_safe        = state.get("is_safe"),
    )
    session.add(email)
    # session.flush()  # Use flush to get the ID without closing the transaction
    session.commit()   # Only commit here if this is a standalone operation
    return email


def save_sent_email(session: Session, sender_id: int, thread_id: str,state: dict) -> SentEmail:
    """
    Persists the final outbound reply sent by the agent.
    """
    # Ensure we don't save an empty email if the agent decided not to reply
        
    email = SentEmail(
        sender_id       = sender_id,
        thread_id    = thread_id,
        recipient_email = state.get("sender_email_id"),
        subject         = state.get("reply_subject") or f"Re: {state.get('sender_subject')}",
        body            = state.get("reply_email_body"),
    )
    session.add(email)
    session.commit()
    return email

