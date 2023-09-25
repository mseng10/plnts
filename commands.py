import Plant
import json

class Commands:

    @staticmethod
    def __check__():
       def check(plant: Plant):
            if not plant.needs_water and plant.flag_for_water():
                print(f"{plant} needs water")
       update_plants(check())





