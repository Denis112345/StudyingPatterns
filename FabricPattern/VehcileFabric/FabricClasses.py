from abc import ABC, abstractmethod
from VehicleClasses import AbstractVehicle, Car, Bike
from enum import Enum


class Vehicles(Enum):
    CAR = 'car'
    BIKE = 'bike'

class AbstractVehicleFactory(ABC):
    """Абстрактный класс для создания фабрик"""
    @abstractmethod
    def create_vehical(self) -> AbstractVehicle:
        """Общий интерфейс для фабрик создания транспорта"""
        pass

class CarFactory(AbstractVehicleFactory):
    def create_vehical(self) -> Car:
        return Car()
    
class BikeFactory(AbstractVehicleFactory):
    def create_vehical(self) -> Bike:
        return Bike()
    

if __name__ == '__main__':
    type_vehicel = input('Введите тип транспорта для запуска: ').lower()

    if type_vehicel == Vehicles.CAR:
        car_factory = CarFactory()
        car = car_factory.create_vehical()
        car.drive()

    if type_vehicel == Vehicles.BIKE:
        bike_facory = BikeFactory()
        bike = bike_facory.create_vehical()
        bike.drive()

