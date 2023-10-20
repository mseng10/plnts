from model import Model

class Plant(Model):
    """Plant model."""
    def __init__(self, genus, name, type, watering, last_water=None, needs_water=None):
        super().__init__()
        self.genus: str = genus
        self.type: str = type
        self.name: str = name
        self.watering = watering #int
        self.last_water = datetime.now() if last_water is None else last_water
        self.needs_water = False if needs_water is None else needs_water

    def __repr__(self):
        return f"{self.name} ({self.type}/{self.genus})"
