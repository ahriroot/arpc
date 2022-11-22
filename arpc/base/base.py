import json


class Base:

    def serialize(self):
        return json.dumps(self.__dict__).encode()

    @classmethod
    def deserialize(self, data):
        return self(**json.loads(data.decode()))


class BaseAsync:

    async def serialize(self):
        return json.dumps(self.__dict__).encode()

    @classmethod
    async def deserialize(self, data):
        return self(**json.loads(data.decode()))
