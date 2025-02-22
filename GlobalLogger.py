from abc import ABC
import logging
from datetime import datetime
import json
from dotenv import load_dotenv
import os
from typing import List


class LoggerFormatterJSON(logging.Formatter):
    """Класс для форматирования данных логов под JSON формат"""
    
    def formatTime(self, record: logging.LogRecord) -> str:
        """Функция выдает время лога (record) в формате %Y-%m-%d %H:%M:%S"""

        return datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')

    def format(self, record: logging.LogRecord) -> str:
        """Функция создает JSON лог из record"""

        log_record: dict[str,str] = {
            'asctime': self.formatTime(record),
            'levelname': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'filename': record.filename,
            'lineno': record.lineno,
        }

        return json.dumps(log_record)

class GlobalLoggerManager:
    """Класс глобального логгер менеджера, через который можно получить логер"""

    def __init__(self):
        self.logger_formatter_console: logging.Formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.logger_formatter_file: LoggerFormatterJSON = LoggerFormatterJSON()
    
    def _get_logger_handlers(self, log_file_path: str) -> List[logging.Handler]:
        """Создает хендлеры обработки логов для логгера"""
        console_handler: logging.StreamHandler = logging.StreamHandler()
        file_handler: logging.FileHandler = logging.FileHandler(log_file_path)

        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.ERROR)

        console_handler.setFormatter(self.logger_formatter_console)
        file_handler.setFormatter(self.logger_formatter_file)

        return [console_handler, file_handler]
        
    def get_logger(self, app_name: str, log_file_path: str) -> logging.Logger:
        """Создает и возвращает логгер"""
        logger: logging.Logger = logging.getLogger(app_name)

        logger.setLevel(logging.DEBUG)

        handlers: List[logging.Handler] = self._get_logger_handlers(log_file_path)
        for handler in handlers:
            logger.addHandler(handler)

        return logger

if __name__ == '__main__':
    load_dotenv()

    app_name = os.getenv('APP_NAME')
    log_file_path = os.getenv('LOG_FILE_PATH')

    logger: logging.Logger = GlobalLoggerManager().get_logger(app_name, log_file_path)
    logger.info('Logger created successfally')