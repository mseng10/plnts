import json


class Model(object):
    """Abstract model class (stored in the db)."""

    def __init__(self) -> None:
        pass

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(class_name, data: str) -> any:
        return class_name(**json.loads(data))
