import Command
import json



class Create(Command):
    @staticmethod
    def process():
        def water(plant: Plant):
            plant.water()
        update_plants(water())