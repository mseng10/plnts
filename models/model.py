import json


class Model(object):
    def __init__(self):
        pass

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(class_name, data: str) -> any:
        return class_name(**json.loads(data))
