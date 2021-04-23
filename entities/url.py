from datetime import datetime
from pydantic import BaseModel, Field


class URL(BaseModel):
    user_id: int
    url: str
    short_url: str
    days_to_expire: int = 120
    created_at: datetime = Field(default_factory=datetime.utcnow)

