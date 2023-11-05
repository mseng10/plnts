from commands.command import Command
from models.plant import Plant
from util.db_util import DBUtil
from util.util import Util


class Create(Command):
    def __int__(self):
        super().__init__()

    def process(self):
        super().process()
        plants = DBUtil.read_plants()

        print("Current Geni (lol):")
        for p in plants:
            print(f"\t{p.genus}")
        genus: str = input("Genus? ")

        print("Current Types in Geni (lol):")
        for p in plants:
            if genus == p.genus:
                print(f"\t{p.type}")
        type: str = input("Type? ")

        print("Current Names in Type:")
        for p in plants:
            if genus == p.genus and type == p.type:
                print(f"\t{p.name}")
        name: str = input("Name? ")

        total: int = 0
        for p in plants:
            if genus == p.genus and type == p.type and name == p.name:
                total += 1

        watering: int = int(input("Water how often (days)? "))
        cost: int = int(input("Cost?"))
        last_water: str = input("Last Water (MM-DD-YYYY)? ")
        print(len(last_water))

        plant = Plant(
            id=total + 1,
            genus=genus,
            name=name,
            type=type,
            watering=watering,
            cost=cost,
            last_water=last_water,
        )
        print(plant)
        if not Util.confirm("Create?"):
            return

        plants.append(plant)
        DBUtil.load_plants(plants)
