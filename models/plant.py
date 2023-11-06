from models.model import Model
from datetime import datetime, timedelta


class Plant(Model):
    """Plant model."""

    def __init__(
        self,
        id: int,
        genus: str,
        name: str,
        type: str,
        watering: int,
        cost: int,
        last_water: str,
    ) -> None:  # duh
        super().__init__()
        self.genus: str = genus
        self.type: str = type
        self.name: str = name
        self.id: int = id
        self.watering: int = watering  # days
        self.cost: int = cost  # $
        self.last_water: str = last_water  # 10-10-2023

    def __repr__(self) -> str:
        return f"{self.name} ({self.type}/{self.genus})"

    def needs_water(self) -> bool:
        """Does the plant need water?"""
        return datetime.now() > datetime.strptime(
            self.last_water, "%m-%d-%Y"
        ) + timedelta(days=self.watering)

    def water(self) -> None:
        """Water the plant."""
        self.last_water: str = datetime.now().strftime("%m-%d-%Y")
