from sqlalchemy import Column, Integer, String, JSON, Enum, DateTime, func
from enum import Enum as PyEnum
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Status(PyEnum):
    QUEUED = "queued"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True)
    type = Column(String)

    status = Column(
        Enum(Status),
        default=Status.QUEUED,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    error_message = Column(String, nullable=True)
    payload = Column(JSON)
    attempts = Column(Integer, default=0)