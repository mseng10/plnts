from commands.command import Command
from models.plant import Plant
from util.db_util import DBUtil
from util.util import Util


class Update(Command):
    """Update a plant command."""

    def __init__(self) -> None:
        Command.__init__(self, key="update", description="Update a plant.")

    def process(self) -> None:
        super().process()
        DBUtil.update_plants(self._process)

    def _process(self, plants: list[Plant]) -> None:
        """Prompts the user to update the plants."""
        # TODO: CLEAN UP
        filtered_plants: list[Plant] = plants
        print("Current Geni (lol):")
        for p in filtered_plants:
            print(f"\t{p.genus}")
        genus: str = input("Genus? ")
        filtered_plants = [p for p in filtered_plants if p.genus == genus]

        print("Current Types in Geni (lol):")
        for p in filtered_plants:
            print(f"\t{p.type}")
        type: str = input("Type? ")
        filtered_plants = [p for p in filtered_plants if p.type == type]

        print("Current Names in Type:")
        for p in filtered_plants:
            print(f"\t{p.name}")
        name: str = input("Name? ")
        filtered_plants = [p for p in filtered_plants if p.name == name]

        print("Which one?")
        for p in filtered_plants:
            print(f"\t{p.id}")
        id: int = int(input("ID? "))
        filtered_plants = [p for p in filtered_plants if p.id == id]

        plant = filtered_plants[0]
        print("--------------------")
        print(f"{plant} to update.")
        while Util.confirm("Continue to update field on plant"):
            self.__run_plant_update(plant)

        print("Updating is over..")
        print()

    def __run_plant_update(self, plant: Plant) -> None:
        """Prompt the user for a field and value to update on the provided plant."""
        print("--------------------")
        print(f"Current {plant} data:")
        for key in plant.__dict__:
            print(f"{key} - {plant.__dict__[key]}")

        key: str = input("Which field to update? ")
        if key not in plant.__dict__.keys():
            print("Field not in available fields.")
            print("Exiting..")  # TODO: Retry?
            return
        value = input("Value? ")
        DBUtil.update_model(plant, key, value)
        print("Successfully updated plant!")
        print("--------------------")
