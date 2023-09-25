import Command
import json



class Create(Command):
    def __int__(self):
        print("")

    @staticmethod
    def process():
        f = open('data/plants.json')
        plants = json.load(f)

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
        # TODO: Does not support doubles
        plants.append(plant.to_json())

        json.dump(plants, 'data/plants.json', indent=4)
        # Closing file
        f.close()