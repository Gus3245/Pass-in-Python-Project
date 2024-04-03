from src.models.settings.base import Base
from sqlalchemy import collum, String, Integer

class Events(Base):
    __tablename__ = "events"

    id = collum(String, primary_key=True)
    title = collum(String, nullable=False)
    details = collum(String)
    slug = collum(String, nullable=False)
    maximum_attendees = collum(Integer)


