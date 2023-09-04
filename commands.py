import Plant
import json

class Commands:

    @staticmethod
    def __create__():
        f = open('data/plants.json')
        plants = json.load(f)

        genus = input("Genus? ")
        type = input("Type? ")
        name = input("Name? ")
        watering = input("Water how often (e.g. 1)? ") ## days
        print("Currently creating plant: ")
        print(f"Genus: {genus}\nType: {type}\nName: name{name}\nWatering: {watering}")
        yes_or_no = input("Create?")
        if yes_or_no == "no" or yes_or_no == "n":
            return
        plant = Plant(genus=genus, name=name, type=type, watering=watering)
        # TODO: Does not support doubles
        plants.append(plant.to_json())

        json.dump(plants, 'data/plants.json', indent=4)
        # Closing file
        f.close()

    @staticmethod
    def __check__():
       def check(plant: Plant):
            if not plant.needs_water and plant.flag_for_water():
                print(f"{plant} needs water")
       update_plants(check())

    @staticmethod
    def __water__():
        def water(plant: Plant):
            plant.water()
        update_plants(water())


    @staticmethod
    def update_plants(runnable):
        f = open('data/plants.json')
        plants = json.load(f)
        new_plants = []
        for plant in plants:
            plant = Plant.from_json(plant)
            runnable(plant)
            new_plants.append(plant.to_json())

        json.dump(new_plants, 'data/plants.json', indent=4)
        # Closing file
        f.close()





