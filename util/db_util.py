from models.plant import Plant
import json

PLANT_DB = 'data/plants.json'

class DBUtil:
    @staticmethod
    def read_plants() -> list[Plant]:
        f = open(PLANT_DB)
        plants = json.load(f)
        print(plants)
        return [Plant.from_json(Plant, plant) for plant in plants]

    @staticmethod
    def load_plants(plants: list[Plant]):
        with open(PLANT_DB, "w") as outfile:
            json.dump([plant.to_json() for plant in plants], outfile)



