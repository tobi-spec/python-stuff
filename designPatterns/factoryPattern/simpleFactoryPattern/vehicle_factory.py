from bike import Bike
from bus import Bus
from car import Car


def vehicle_factory(vehicle_type: str):
    if vehicle_type is None:
        return None

    match vehicle_type.upper():
        case "BIKE":
            return Bike()
        case "CAR":
            return Car()
        case "BUS":
            return Bus()
