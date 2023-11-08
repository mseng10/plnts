from models.plant import Plant
from models.model import Model
import json
import __main__ as config

PLANT_DB = "data/prod/plants.json"
PLANT_DB_TEST = "data/test/plants.json"


class DBUtil:
    """Various DB helper methods."""

    @staticmethod
    def get_plant_db_path() -> str:
        """Get the plant db path for this configured instance of PMS."""
        return PLANT_DB_TEST if config.TEST_MODE else PLANT_DB

    @staticmethod
    def read_plants() -> list[Plant]:
        """Read plants from the db."""
        f = open(DBUtil.get_plant_db_path())
        plants = json.load(f)
        return [Plant.from_json(Plant, plant) for plant in plants]

    @staticmethod
    def load_plants(plants: list[Plant]):
        """Replace all plants in the db."""
        with open(DBUtil.get_plant_db_path(), "w") as outfile:
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

    @staticmethod
    def update_model(model: Model, key: str, value: any) -> None:
        """Update a field on a model."""
        value_on_model = model.__getattribute__(key)
        if isinstance(value_on_model, int):
            model.__setattr__(key, int(value))
        elif isinstance(value_on_model, float):
            model.__setattr__(key, float(value))
        else:
            model.__setattr__(key, value)
        print(f"{model} had {key} updated to {value}!")
