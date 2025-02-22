from enum import Enum
import sys, os
from pathlib import Path
sys.path.append(os.path.abspath(Path(os.path.dirname(__file__)) / '..'))
from GlobalLogger import GlobalLoggerManager
import logging
from dotenv import load_dotenv
from VehcileFabric.FabricClasses import CarFactory, BikeFactory
from VehcileFabric.VehicleClasses import Car, Bike

class VehicleTypes(Enum):
    CAR: str = 'car'
    BIKE: str = 'bike'

if __name__ == '__main__':
    load_dotenv()

    app_name: str = os.getenv('APP_NAME')
    log_file_path: str = os.getenv('LOG_FILE_PATH')

    logger: logging.Logger = GlobalLoggerManager().get_logger(app_name, log_file_path)

    logger.info('Программа запущена')
    
    type_vehicel: str = input('Введите тип транспорта для запуска: ').lower()

    logger.info('Пользователь ввел тип транспорта')

    if type_vehicel.upper() in VehicleTypes.__members__:
        if type_vehicel == VehicleTypes.CAR.value:
            car_factory: CarFactory = CarFactory()
            car: Car = car_factory.create_vehical()
            info: str = car.drive()
            
            logger.info(info)

        if type_vehicel == VehicleTypes.BIKE.value:
            bike_facory: BikeFactory = BikeFactory()
            bike: Bike = bike_facory.create_vehical()
            info: str = bike.drive()

            logger.info(info)
    else:
        logger.warning('Пожалуйста введите валидный тип траспорта')
    
    logger.info('Прогрмма законичла исполнение')

