import json

class Model:

    def __init__(self):
        print()

    @staticmethod
    def from_json(self, json: dict) -> any:
        pass

    def to_json(self):
        return json.dumps(self.__dict__)