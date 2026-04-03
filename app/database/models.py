from sqlalchemy import (
    Column, Integer, Text, Boolean, DateTime, ForeignKey, String, func

)
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    email      = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())

    received_emails = relationship("ReceivedEmail", back_populates="owner")
    sent_emails     = relationship("SentEmail",     back_populates="sender")


class ReceivedEmail(Base):
    __tablename__ = "received_emails"

    id           = Column(Integer, primary_key=True, autoincrement=True)
    thread_id    = Column(String, nullable=False) 
    owner_id     = Column(Integer, ForeignKey("users.id"), nullable=False)
    sender_email = Column(Text, nullable=False)
    subject      = Column(Text)
    body         = Column(Text)
    received_at  = Column(DateTime, default=func.now())
    is_safe      = Column(Boolean, default=False)
    owner = relationship("User", back_populates="received_emails")


class SentEmail(Base):
    __tablename__ = "sent_emails"

    id              = Column(Integer, primary_key=True, autoincrement=True)
    thread_id    = Column(String, nullable=False) 
    sender_id       = Column(Integer, ForeignKey("users.id"), nullable=False)
    recipient_email = Column(Text,    nullable=False)
    subject         = Column(Text)
    body            = Column(Text)
    sent_at         = Column(DateTime, default=func.now())

    sender = relationship("User", back_populates="sent_emails")


