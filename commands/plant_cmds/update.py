from commands.command import Command
from models.plant import Plant
from util.db_util import DBUtil


class Update(Command):
    """Update a plant command."""

    def __init__(self) -> None:
        Command.__init__(self, key="update", description="Update a plant.")

    def process(self) -> None:
        super().process()
        DBUtil.update_plants(self._process)

    def _process(self, plants: list[Plant]) -> None:
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
        print(f"{plant} to update.")
        kvps = plant.__dict__
        for key in kvps:
            print(f"{key} - {kvps[key]}")

        key: str = input("Which field? ")
        if key not in kvps.keys():
            print("Field not in available fields.")
            return
        value = input("Value? ")
        value_on_model = plant.__getattribute__(key)
        if isinstance(value_on_model, int):
            plant.__setattr__(key, int(value))
        else:
            plant.__setattr__(key, value)

        print("Successfully updated plant!")
