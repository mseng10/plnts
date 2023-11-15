from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from models import Base


class Plant(Base):
    """Plant model."""

    __tablename__ = "plants"

    id = Column(Integer(), primary_key=True)
    genus = Column(String(100), nullable=False)  # should be shared
    type = Column(String(100), nullable=False)  # should be shared
    name = Column(String(100), nullable=False)
    watering = Column(Integer())
    cost = Column(Integer())

    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    watered_on = Column(DateTime(), default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.name} ({self.type}/{self.genus})"

    # def needs_water(self) -> bool:
    #     """Does the plant need water?"""
    #     return datetime.now() > datetime.strptime(
    #         self.last_water, "%m-%d-%Y"
    #     ) + timedelta(days=self.watering)
    #
    # def water(self) -> None:
    #     """Water the plant."""
    #     self.last_water: str = datetime.now().strftime("%m-%d-%Y")
