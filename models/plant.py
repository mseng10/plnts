import datatime

class Plant:
    def __init__(self, genus, name, type, watering, last_water=None, needs_water=None):
        self.genus = genus #enum?
        self.name = name # str
        self.type = type
        self.watering = watering #int
        self.last_water = datetime.now() if last_water is None else last_water
        self.needs_water = False if needs_water is None else needs_water

    def __repr__(self):
        return f"{self.name} ({self.type}/{self.genus})"

    def to_json(self):
        return {
            "genus": self.genus,
            "name": self.name,
            "type": self.type,
            "watering": self.watering,
            "last_water": self.last_water,
            "needs_water": self.needs_water
        }
    @statidmethod
    def from_json(self, json):
        return Plant(
            genus=json["genus"],
            name=json["name"],
            type=json["type"],
            watering=json["watering"],
            last_water=json["last_water"], ## TRICKY
            needs_water=json["needs_water"]
        )

    def flag_for_water(self):
        last_water = datetime.datetime.strptime(self.last_water, "%m/%d/%y")
        need_date = last_water + datetime.timedelta(days=self.watering)
        curr_date = datetime.datetime.strptime(datatime.now(), "%m/%d/%y")
        self.needs_water = curr_date == need_date
        return self.needs_water

    # Actually water the plant, update it's last_water in json
    def water(self):
        self.last_water = datetime.now()
        self.needs_water = False
