import Command
import json



class Water(Command):
    def __int__(self):
        print("")

    @staticmethod
    def process():
        def water(plant: Plant):
            plant.water()
        update_plants(water())