from designPatterns.builderPattern.CarBuilder import CarBuilder

car = CarBuilder()\
    .id(1)\
    .brand("VW")\
    .model("Polo")\
    .color("Blue")\
    .build()

print(car)
