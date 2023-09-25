import json
import Plant

class Command():

    @abstractmethod
    def process(self):

    @staticmethod
    def update_db(runnable):
        f = open('data/plants.json')
        plants = json.load(f)
        new_plants = []
        for plant in plants:
            plant = Plant.from_json(plant)
            runnable(plant)
            new_plants.append(plant.to_json())

        json.dump(new_plants, 'data/plants.json', indent=4)
        f.close()