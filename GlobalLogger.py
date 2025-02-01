from abc import ABC
import logging
from datetime import datetime
import json
from dotenv import load_dotenv
import os
from typing import List


class LoggerFormatterJSON(logging.Formatter):
    def formatTime(self, record: logging.LogRecord, datefmt: str = None) -> str:
        return datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')

    def format(self, record: logging.LogRecord) -> str:
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
    def __init__(self):
        self.logger_formatter_console: logging.Formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.logger_formatter_file: LoggerFormatterJSON = LoggerFormatterJSON()
    
    def _get_logger_handlers(self) -> List[logging.Handler]:
        load_dotenv()

        console_handler: logging.StreamHandler = logging.StreamHandler()
        file_handler: logging.FileHandler = logging.FileHandler(os.getenv('LOG_FILE'))

        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.ERROR)

        console_handler.setFormatter(self.logger_formatter_console)
        file_handler.setFormatter(self.logger_formatter_file)

        return [console_handler, file_handler]
        
    def get_logger(self) -> logging.Logger:
        logger: logging.Logger = logging.getLogger(os.getenv('APP_NAME'))

        logger.setLevel(logging.DEBUG)

        handlers: List[logging.Handler, logging.Handler] = self._get_logger_handlers()
        for handler in handlers:
            logger.addHandler(handler)

        return logger

if __name__ == '__main__':
    logger = GlobalLoggerManager().get_logger()
    logger.info('Logger successfall create')