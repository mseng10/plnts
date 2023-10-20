from models.plant import Plant
import json

PLANT_DB = 'data/plants.json'

@staticmethod
def read_plants() -> list[Plant]:
    f = open(PLANT_DB)
    plants = json.load(f)
    return [Plant.from_json(plant) for plant in plants]

@staticmethod
def load_plants(plants: list[Plant]):
    json.dump([plant.to_json() for plant in plants], PLANT_DB, indent=4)



