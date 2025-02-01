from abc import ABC, abstractmethod
from .VehicleClasses import AbstractVehicle, Car, Bike


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
