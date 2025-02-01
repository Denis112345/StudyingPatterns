from abc import ABC, abstractmethod


class AbstractVehicle(ABC):
    """Абастрактный класс для всех транспортных средств"""

    @abstractmethod
    def drive(self) -> None:
        """Абстрактный метод который
        является общим интерфейсов и
        должен быть реализован во всех
        дочерних классах"""
        pass

class Car(AbstractVehicle):
    def drive(self):
        return "The car left successfully"

class Bike(AbstractVehicle):
    def drive(self):
        return "The bike left successfully"
    
if __name__ == '__main__':
    print('VihicleClasses')