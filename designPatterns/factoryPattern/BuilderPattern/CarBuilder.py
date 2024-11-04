from designPatterns.factoryPattern.BuilderPattern.Car import Car


class CarBuilder:
    def __init__(self):
        self._color = None
        self._model = None
        self._id = None
        self._brand = None

    def id(self, id):
        self._id = id
        return self

    def brand(self, brand):
        self._brand = brand
        return self

    def model(self, model):
        self._model = model
        return self

    def color(self, color):
        self._color = color
        return self

    def build(self):
        return Car(self.id, self.brand, self.model, self.color)

