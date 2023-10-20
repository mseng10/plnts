import Command
import json
from models.plant import Plant
from util.db_util import read_plants
class Create(Command):

    def __int__(self):
        super().__init__('create')

    @staticmethod
    def process():
        plants = read_plants()

        genus = input("Genus? ")
        type = input("Type? ")
        name = input("Name? ")
        watering = input("Water how often (e.g. 1)? ")  ## days
        print("Currently creating plant: ")
        print(f"Genus: {genus}\nType: {type}\nName: name{name}\nWatering: {watering}")
        yes_or_no = input("Create?")
        if yes_or_no == "no" or yes_or_no == "n":
            return
        plant = Plant(genus=genus, name=name, type=type, watering=watering)
        print(plant)

        # TODO: Does not support doubles
        plants.append(plant.to_json())

        json.dump(plants, 'data/plants.json', indent=4)
        # Closing file
        f.close()