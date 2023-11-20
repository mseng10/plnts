from processes.process import Process
from models.plant import Plant
from util.util import Util
from datetime import datetime

from db import Session


class Create(Process):
    def __init__(self) -> None:
        Process.__init__(
            self, key="create", description="Create a plant and add it to the clan."
        )

    def process(self) -> None:
        super().process()
        db = Session()

        query = db.query(Plant)
        plants: list[Plant] = query.all()
        print("Current Geni (lol):")
        for p in query.all():
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

        watered_on_str: str = input("Last Water (MM-DD-YYYY)? ")
        if len(watered_on_str) == 0:
            watered_on = datetime.now()
        else:
            month, day, year = map(int, watered_on_str.split("-"))
            watered_on = datetime.date(year, month, day)

        plant = Plant(
            genus=genus,
            name=name,
            type=type,
            watering=watering,
            cost=cost,
            watered_on=watered_on,
        )
        print(plant)
        if not Util.confirm("Create? "):
            # TODO : Edit capability's?
            return

        db.add(plant)
        db.commit()
