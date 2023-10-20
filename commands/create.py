from commands.command import Command
from models.plant import Plant
from util.db_util import DBUtil
from util.util import Util
class Create(Command):

    def __int__(self):
        super().__init__('create')

    def process(self):
        plants = DBUtil.read_plants()

        print("Current Geni (lol):")
        for p in plants: print(f"\t{p.genus}")
        genus: str = input("Genus? ")

        print("Current Types in Geni (lol):")
        for p in plants:
            if genus == p.genus:
                print(f"\t{p.type}")
        type = input("Type? ")
        
        for p in plants: print(f"\t{p.name}")
        name = input("Name? ")

        watering = input("Water how often (e.g. 1)? ")

        plant = Plant(genus=genus, name=name, type=type, watering=watering)
        print(plant)
        if not Util.confirm("Create?"):
            return

        plants.append(plant)
        DBUtil.load_plants(plants)
