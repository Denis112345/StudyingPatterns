from VehcileFabric.FabricClasses import CarFactory, BikeFactory
from enum import Enum


class Vehicles(Enum):
    CAR = 'car'
    BIKE = 'bike'

if __name__ == '__main__':
    type_vehicel = input('Введите тип транспорта для запуска: ').lower()
    if type_vehicel == Vehicles.CAR.value:
        car_factory = CarFactory()
        car = car_factory.create_vehical()
        print(car.drive())

    if type_vehicel == Vehicles.BIKE.value:
        bike_facory = BikeFactory()
        bike = bike_facory.create_vehical()
        print(bike.drive())
