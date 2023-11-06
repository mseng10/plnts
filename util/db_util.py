from models.plant import Plant
import json

PLANT_DB = "data/plants.json"


class DBUtil:
    """Various DB helper methods."""

    @staticmethod
    def read_plants() -> list[Plant]:
        """Read plants from the db."""
        f = open(PLANT_DB)
        plants = json.load(f)
        return [Plant.from_json(Plant, plant) for plant in plants]

    @staticmethod
    def load_plants(plants: list[Plant]):
        """Replace all plants in the db."""
        with open(PLANT_DB, "w") as outfile:
            json.dump([plant.to_json() for plant in plants], outfile)

    @staticmethod
    def update_plants(runnable) -> None:
        """Update plants all plants in the db."""
        plants: list[Plant] = DBUtil.read_plants()
        runnable(plants)
        DBUtil.load_plants(plants)

    @staticmethod
    def get_plants_and_consume(runnable) -> None:
        """Gets and performs the method on them. Maybe a little overkill to have this method."""
        plants: list[Plant] = DBUtil.read_plants()
        runnable(plants)
