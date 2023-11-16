from processes.process import Process
from models.plant import Plant
from util.util import Util
import datetime

from db import Session


class Create(Process):
    def __init__(self) -> None:
        Process.__init__(
            self, key="create", description="Create a plant and add it to the clan."
        )

    def process(self) -> None:
        super().process()
        db = Session()

        plants: list[Plant] = db.query(Plant).all()
        print("Current Geni (lol):")
        for p in plants:
            print(f"\t{p.genus}")
        genus: str = self.input("Genus? ")

        print("Current Types in Geni (lol):")
        for p in plants:
            if genus == p.genus:
                print(f"\t{p.type}")
        type: str = self.input("Type? ")

        print("Current Names in Type:")
        for p in plants:
            if genus == p.genus and type == p.type:
                print(f"\t{p.name}")
        name: str = self.input("Name? ")

        watering: int = int(self.input("Water how often (days)? "))
        cost: int = int(self.input("Cost($)? "))

        last_water_str: str = input("Last Water (MM-DD-YYYY)? ")
        month, day, year = map(int, last_water_str.split("-"))
        last_water = datetime.date(year, month, day)

        plant = Plant(
            genus=genus,
            name=name,
            type=type,
            watering=watering,
            cost=cost,
            last_water=last_water,
        )
        print(plant)
        if not Util.confirm("Create? "):
            # TODO : Edit capability's?
            return

        db.add(plant)
        db.commit()
