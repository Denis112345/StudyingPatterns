from VehcileFabric.FabricClasses import CarFactory, BikeFactory
from enum import Enum
import sys, os
from pathlib import Path
sys.path.append(os.path.abspath(Path(os.path.dirname(__file__)) / '..'))
from GlobalLogger import GlobalLoggerManager
import logging
from dotenv import load_dotenv

class VehicleTypes(Enum):
    CAR = 'car'
    BIKE = 'bike'

if __name__ == '__main__':
    load_dotenv()

    app_name = os.getenv('APP_NAME')
    log_file_path = os.getenv('LOG_FILE_PATH')

    logger: logging.Logger = GlobalLoggerManager().get_logger(app_name, log_file_path)
    logger.info('Programm started')
    
    type_vehicel = input('Введите тип транспорта для запуска: ').lower()

    logger.info('User input type vehical')

    if type_vehicel.upper() in VehicleTypes.__members__:
        if type_vehicel == VehicleTypes.CAR.value:
            car_factory = CarFactory()
            car = car_factory.create_vehical()
            info = car.drive()
            
            logger.info(info)

        if type_vehicel == VehicleTypes.BIKE.value:
            bike_facory = BikeFactory()
            bike = bike_facory.create_vehical()
            info = bike.drive()

            logger.info(info)
    else:
        logger.warning('Please input valide type of Vehicle')
    
    logger.info('Programm finished')

